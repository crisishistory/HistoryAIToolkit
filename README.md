# HistoryAIToolkit

AI toolkit for professional and amateur historians, and for anyone who wishes to contribute to the recording of history by and for the community.

## Sample Data

Taken from [this interview](https://wayback.archive-it.org/14173/20200910203008mp_/http://oralhistory.nypl.org/interviews/martine-barrat-vlsin5
).

```bash
wget https://wayback.archive-it.org/14173/20200910203008/https://s3.amazonaws.com/oral-history/audio/Martine+Barrat_FINAL.mp3
```

Next, get the first 5 minutes of data:

```bash
python interviewkit/sampler.py data/Martine+Barrat_FINAL.mp3 2
```

* [ ] Put it in data/

## Demo

The scope of the demo we hope to complete at PyCon UK is:

* [ ] Take a 5-min audio file as input in main.py
* [ ] Transcribe the audio file using OpenAI API
* [ ] Save the transcription to a text file
* [ ] Print the transcription to the console
* [ ] Pass the text to the OpenAI API to generate a list of follow-up interview questions
* [ ] Print the questions to the console
