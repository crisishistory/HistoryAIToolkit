# HistoryAIToolkit

AI toolkit for professional and amateur historians, and for anyone who wishes to contribute to the recording of history by and for the community.

Join our Discord server: https://discord.gg/WvqytcHfnD

## Project goals and scope

Some time ago Audrey come in contact with a group of historians working on interviews of survivors of relevant historical events, with the goal of avoiding the loss of this highly valuable first-hand knowledge down the timeline.  

Interviews are conducted by:

* Experienced historians
* Less experienced historians, students, and volunteer community researchers under the mentorship of experienced historians

Experienced historical interviewers are good at asking follow-up questions in a way that makes an interviewee not just feel comfortable, but enjoy telling their stories in vivid, relatable ways as a contribution to the historical record.

However, less experienced interviewers may feel intimidated by narrators with a strong presence. Sometimes a junior historian interviewing a famous person blanks out while trying to come up with good follow-up questions. Or they risk asking questions that may make the interviewee uncomfortable, which may led to loss of the opportunity to collect good historical materials.

The goal of the project is to help historians and narrators in various ways:

* Help community history researchers of all levels be better, friendlier interviewers
* Help those with interesting historial experiences tell their stories and enjoy the process
* Help survivors telling difficult stories feel at ease, with kindness, empathy, and respect

From a technical perspective, this involves:

* Providing tools to process past audio and video interviews
  * Slicing/editing of snippets of interest
  * Conversion to high-quality text transcripts
* Providing tools to generate interview questions from past or realtime interviews 
  * Feeding transcript text to an LLM
  * Using an LLM to help to generate interesting, fun, friendly, and appropriate follow-up questions to help interviewers ask great questions

Interviews can be about surviving adversity, but they can also be about witnessing special historical moments. For example, an oral history interview could be about working with famous computer scientists and witnessing the history of computing.

## Status

The code in here is a proof-of-concept to give you an idea of what we're building. It partially works. The code, documentation, and tests are still a bit unstable and need a lot of love. We need all the help we can get.

## Prototype

The scope of the prototype we hope to complete in the 2-3 weeks following PyCon UK is:

* [ ] Take interview audio in from main.py
  * [ ] Realtime microphone input
  * [x] Mock input from a short audio file simulating a piece of an interview
* [x] Transcribe the interview audio using a (preferably free) transcription package or API
* [x] Save the transcription to a text file
* [ ] Print the transcription to the console
* [ ] Pass the text to a (preferably free) LLM package or API to generate a list of follow-up interview questions
* [ ] Print the questions to the console

## Example Data

To experiment with this project using a recorded interview for test purposes, download one or more of the audio files from:
https://www.kaggle.com/datasets/audreyfeldroy/oral-history-audio-interviews

Sample oral history interviews, some with transcripts we can work with:
* https://wayback.archive-it.org/14173/20200827171043/http://transcribe.oralhistory.nypl.org/

## Getting Started

See docs/getting_started.rst
