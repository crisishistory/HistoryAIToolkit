# HistoryAIToolkit

AI toolkit for professional and amateur historians, and for anyone who wishes to contribute to the recording of history by and for the community.

Join our Discord server: [discord.gg/WvqytcHfnD](https://discord.gg/WvqytcHfnD)

## Project goals and scope

Some time ago Audrey came in contact with a group of historians working on interviews of people with first-hand knowledge of significant historical events. These historians are part of a larger international research community collecting historically-important stories. The hope is to prevent highly valuable first-hand narratives from being lost down the timeline. 

Narratives can be from world leaders, community organizers, witnesses of technological developments, notable people, elders, immigrants, participants of historical events, natural disaster survivors, etc. 

Interviews are conducted by:

* Experienced historians
* Less experienced historians, students, and volunteer community researchers under the mentorship of experienced historians

Experienced historical interviewers are good at asking follow-up questions in a way that makes an interviewee feel comfortable and enjoy telling their stories in vivid, relatable ways as a contribution to the historical record. Less experienced interviewers may feel intimidated by interviewees with a strong presence or not know the full historical context to use in subsequent interview questions. 

Regardless of experience, all interviewers run the risk of omitting questions that then become a lost opportunity to collect complete histories. The goal of the project is to help all types of historians and interviewees in various ways:

* Assist community history researchers, of all levels, making them more informed and ready to engage with the interviewees and their oral history testimonies
* Aid those with interesting historical experiences confidently tell their stories and enjoy the process
* Put survivors telling difficult stories at ease by skillfully listening with empathy and respect 

From a technical perspective, this involves:

* Providing tools to process past audio and video interviews
  * Slicing/editing of snippets of interest
  * Conversion to high-quality text transcripts
* Providing tools to generate interview questions from past or realtime interviews 
  * Feeding transcript text to an LLM
  * Using an LLM to help to generate meaningful, insightful, and appropriate follow-up questions to help interviewers create the most historically complete record.

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
[kaggle.com/datasets/audreyfeldroy/oral-history-audio-interviews](https://www.kaggle.com/datasets/audreyfeldroy/oral-history-audio-interviews)

Sample oral history interviews, some with transcripts we can work with:
* [wayback.archive-it.org/14173/20200827171043/http://transcribe.oralhistory.nypl.org/](https://wayback.archive-it.org/14173/20200827171043/http://transcribe.oralhistory.nypl.org/)

## Getting Started

First install the project using the [installation instructions](https://historyaitoolkit.readthedocs.io/en/latest/getting-started/). Then to use the command-line interface, run this in your terminal: 

```
hist --help
```

## Contributors

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/audreyfeldroy">
            <img src="https://avatars.githubusercontent.com/u/74739?v=4" width="100;" alt="audreyfeldroy"/>
            <br />
            <sub><b>Audrey Roy Greenfeld</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/pydanny">
            <img src="https://avatars.githubusercontent.com/u/62857?v=4" width="100;" alt="pydanny"/>
            <br />
            <sub><b>Daniel Roy Greenfeld</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Subramaniam-dot">
            <img src="https://avatars.githubusercontent.com/u/66780405?v=4" width="100;" alt="Subramaniam-dot"/>
            <br />
            <sub><b>SUBRAMANIAM SUBRAMANIAN MURUGESAN</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/danielmaclaren">
            <img src="https://avatars.githubusercontent.com/u/101112838?v=4" width="100;" alt="danielmaclaren"/>
            <br />
            <sub><b>Dtmaclaren</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/kaqmak">
            <img src="https://avatars.githubusercontent.com/u/7051207?v=4" width="100;" alt="kaqmak"/>
            <br />
            <sub><b>Per Lunnemann Hansen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Bchass">
            <img src="https://avatars.githubusercontent.com/u/34097574?v=4" width="100;" alt="Bchass"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/VivekKumarKamal">
            <img src="https://avatars.githubusercontent.com/u/118813447?v=4" width="100;" alt="VivekKumarKamal"/>
            <br />
            <sub><b>Vivek Kumar Kamal</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/heymanpreet">
            <img src="https://avatars.githubusercontent.com/u/22243845?v=4" width="100;" alt="heymanpreet"/>
            <br />
            <sub><b>Manpreet Chawla</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/RalphHuber">
            <img src="https://avatars.githubusercontent.com/u/35894863?v=4" width="100;" alt="RalphHuber"/>
            <br />
            <sub><b>Ralph Sinnhuber</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/DominikBalga">
            <img src="https://avatars.githubusercontent.com/u/77111779?v=4" width="100;" alt="DominikBalga"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/willjos">
            <img src="https://avatars.githubusercontent.com/u/111782618?v=4" width="100;" alt="willjos"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/ZoePosnette">
            <img src="https://avatars.githubusercontent.com/u/109586022?v=4" width="100;" alt="ZoePosnette"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td></tr>
<tr>
    <td align="center">
        <a href="https://github.com/Night-Amber3301">
            <img src="https://avatars.githubusercontent.com/u/99665583?v=4" width="100;" alt="Night-Amber3301"/>
            <br />
            <sub><b>Pratibhanu Jarngal</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/ProfessorTerrence">
            <img src="https://avatars.githubusercontent.com/u/145303482?v=4" width="100;" alt="ProfessorTerrence"/>
            <br />
            <sub><b>ProfessorTerrence</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Rjchauhan18">
            <img src="https://avatars.githubusercontent.com/u/113838908?v=4" width="100;" alt="Rjchauhan18"/>
            <br />
            <sub><b>Rahul Chauhan</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/raul-testpad">
            <img src="https://avatars.githubusercontent.com/u/107547903?v=4" width="100;" alt="raul-testpad"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/ayushawasthi24">
            <img src="https://avatars.githubusercontent.com/u/116417909?v=4" width="100;" alt="ayushawasthi24"/>
            <br />
            <sub><b>Null</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/ShujiHanma">
            <img src="https://avatars.githubusercontent.com/u/102284492?v=4" width="100;" alt="ShujiHanma"/>
            <br />
            <sub><b>Deluxe.</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->
