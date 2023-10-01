try: 
    import whisper
except ImportError:
    print("Please install Whisper: pip install git+https://github.com/openai/whisper.git")
    exit(1)

from whisper.utils import get_writer
from pydantic import BaseModel

class Transcript(BaseModel):
    """The Transcript entity represents the transcript of an interview."""

    content: str

def main() -> None:

    model = whisper.load_model("base")

    # Change this file path to be the location of the audio file, or connect it to the slicer.py file. The audio used can be a .mp3 or a .wav file
    AUDIO_LOCATION = "/workspaces/HistoryAIToolkit/interviewkit/"
    AUDIO_FILENAME = "sampled-2-Martine+Barrat_FINAL.mp3"

    result = model.transcribe((AUDIO_LOCATION + AUDIO_FILENAME), fp16=False)

    transcript_output_location = "./"

    # Setting some initial options values for the .txt output file
    txt_file_options = {
        'max_line_width': 50, # the maximum number of characters in a line before breaking the line
        'max_line_count': 1, # the maximum number of lines in a segment
        'highlight_words': False # underline each word as it is spoken in srt and vtt
    }

    # Save as a .txt file without line breaks, name of the file could be changed with the slicer.py name of audio file
    # with open((AUDIO_FILENAME + ".txt"), "w", encoding="utf-8") as txt:
    #    txt.write(result["text"])   

    # Save as a .txt file with hard breaks, added for readability to user
    txt_writer = get_writer("txt", transcript_output_location)
    txt_writer(result, AUDIO_FILENAME, txt_file_options)

if __name__ == "__main__":
    main()