from random import choice
from interviewee import Interviewee
from enum import StrEnum, auto
from transcript import Transcript


class Status(StrEnum):
    IN_PROGRESS = auto()
    RECORDED = auto()
    RECORDING = auto()
    TRANSCRIBED = auto()


class Interview(object):
    """An interview between an Interviewee and an Interviewer."""

    def __init__(self, interviewee: Interviewee, transcript: Transcript):
        self.interviewee = interviewee
        self.status = Status.IN_PROGRESS

    def start_recording(self) -> None:
        """Start recording audio."""
        self.status = Status.RECORDING

    def stop_recording(self) -> None:
        """Stop recording audio."""
        self.status = Status.RECORDED

    def start_transcription(self) -> None:
        print("transcribing")
        self.status = "Transcribing"

    def add_to_transcript(self, speech: str) -> None:
        self.transcript.append(speech)

    def stop_transcription(self) -> None:
        self.status = Status.TRANSCRIBED

        # Combine list of transcribed text into a single string
        self.transcript = " ".join(self.transcript)

    def suggest_questions(self) -> str:
        """suggest questions based on the transcript content."""
        suggested_questions = self.generate_questions(self.transcript)
        return suggested_questions

    def generate_questions(self, content: str) -> list[str]:
        """generate questions, and return them."""

        #TODO
        response = None

        # Extract and return the generated questions
        generated_questions = [choice["text"].strip() for choice in response.choices]
        return generated_questions
