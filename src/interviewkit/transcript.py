from pathlib import Path
from rich.console import Console
import sys
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

try:
    import whisper
except ImportError:
    print("Please install Whisper: pip install openai-whisper")
    exit(1)

from whisper.utils import get_writer
from pydantic import BaseModel

console = Console()

class Transcript(BaseModel):
    """The Transcript entity represents the transcript of an interview."""
    content: str

# # Securely get your credentials
# PAT = os.getenv('CLARIFAI_PAT')
# USER_ID = os.getenv('CLARIFAI_USER_ID')
# APP_ID = os.getenv('CLARIFAI_APP_ID')
# MODEL_ID = os.getenv('CLARIFAI_MODEL_ID')
# MODEL_VERSION_ID = os.getenv('CLARIFAI_MODEL_VERSION_ID')
PAT = ''
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
USER_ID = 'meta'
APP_ID = 'Llama-2'
# Change these to whatever model and text URL you want to use
MODEL_ID = 'llama2-70b-chat'
MODEL_VERSION_ID = 'acba9c1995f8462390d7cb77d482810b'

def generate_questions(transcript_chunk):
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)
    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=transcript_chunk
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    output = post_model_outputs_response.outputs[0]
    return output.data.text.raw

def transcribe_from_paths(source: Path, target: Path) -> None:
    console.print("Loading whisper base model...")
    model = whisper.load_model("base")

    with console.status("Transcribing audio file..."):
        result = model.transcribe((str(source)), fp16=False)

    # Setting some initial options values for the .txt output file
    txt_file_options = {
        "max_line_width": 50,  
        "max_line_count": 1,
        "highlight_words": False,  
    }

    # Save as a .txt file with hard breaks, added for readability to user
    console.print("Saving transcript as a .txt file...")
    txt_writer = get_writer("txt", str(target))
    txt_writer(result, source.name, txt_file_options)

    console.print("Transcript saved to:")
    console.print(f"    [green bold]{target / source.name}.txt[/green bold]")

    # Generate questions from the transcript
    transcript_chunk = result['text']  # Assuming 'result' contains the transcribed text
    # Debug: Print type and value of transcript_chunk
    print(f"Type of transcript_chunk: {type(transcript_chunk)}")
    print(f"Value of transcript_chunk: {transcript_chunk}")
    
    # Ensure transcript_chunk is a string
    if not isinstance(transcript_chunk, str):
        print("Warning: transcript_chunk is not a string. Trying to convert...")
        transcript_chunk = str(transcript_chunk)
    
    questions = generate_questions(transcript_chunk)
    console.print("Generated Questions:\n", questions)

if __name__ == "__main__":
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    if source.suffix not in [".mp3", ".wav"]:
        raise ValueError("File must be an .mp3 or .wav file")
    transcribe_from_paths(source, target)
