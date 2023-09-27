try: 
    import whisper
except ImportError:
    print("Please install Whisper: pip install git+https://github.com/openai/whisper.git")
    exit(1)

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

    # Save as a TXT file without any line breaks, name of the file could perhaps be changed with the slicer.py name of audio file
    with open((AUDIO_FILENAME + ".txt"), "w", encoding="utf-8") as txt:
        txt.write(result["text"])

if __name__ == "__main__":
    main()