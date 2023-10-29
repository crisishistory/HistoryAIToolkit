from .interview import Interview
from .interviewee import Gender, Interviewee
from .settings import Settings
from .transcript import Transcript


settings = Settings()

if __name__ == "__main__":
    interviewee = Interviewee(name="John Doe", age=60, gender=Gender.MALE)

    transcript_content = "This is the content of the transcript."
    transcript = Transcript(content=transcript_content)

    interview = Interview(interviewee, transcript)

    interview.start_transcription()

    print(f"Interview Status: {interview.status}")
