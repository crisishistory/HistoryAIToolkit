import whisper

MODEL = whisper.load_model("base")

# Change this file path to be the location of the audio file, this can be a .mp3 or a .wav file
AUDIO = "/workspaces/whisper.cpp/samples/sampled-2-Martine+Barrat_FINAL.wav" 

result = MODEL.transcribe(AUDIO, fp16=False)


# Save as a TXT file without any line breaks
with open("transcription.txt", "w", encoding="utf-8") as txt:
    txt.write(result["text"])
