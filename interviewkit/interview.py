from random import choice
from interviewee import Interviewee
import openai
from enum import StrEnum, auto


class Status(StrEnum):
    IN_PROGRESS = auto()
    RECORDED = auto()
    RECORDING = auto()
    TRANSCRIBED = auto()


class Interview(object):
    """An interview between an Interviewee and an Interviewer."""

    def __init__(self, interviewee: Interviewee):
        self.interviewee = interviewee
        self.status = Status.IN_PROGRESS

    def start_recording(self) -> None:
        """Start recording audio."""
        self.status = Status.RECORDING

    def stop_recording(self) -> None:
        """Stop recording audio."""
        self.status = Status.RECORDED

    def start_transcription(self) -> None:
        self.status = "Transcribing"
        self.transcript = []  # TODO: Use object Transcript instead of list?

    def add_to_transcript(self, speech: str) -> None:
        self.transcript.append(speech)

    def stop_transcription(self) -> None:
        self.status = Status.TRANSCRIBED

        # Combine list of transcribed text into a single string
        self.transcript = " ".join(self.transcript)

    def suggest_questions(self) -> str:
        """Use the OpenAI API to suggest questions based on the transcript content."""
        suggested_questions = self.generate_questions(self.transcript)
        return suggested_questions

    def generate_questions(self, content: str) -> list[str]:
        """Call the OpenAI API to generate questions, and return them."""
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate interview questions based on the following transcript:\n{content}\n",
            max_tokens=50,  # Adjust the max tokens as needed
            n=5,  # Number of questions to generate
            stop=None,
            temperature=0.7,  # Adjust the temperature for creativity
        )

        # Extract and return the generated questions
        generated_questions = [choice["text"].strip() for choice in response.choices]
        return generated_questions
