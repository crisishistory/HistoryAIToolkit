from interview import Interview
from interviewee import Interviewee
from transcript import Transcript

if __name__ == "__main__":

    interviewee = Interviewee("John Doe", 60, "Male")

    transcript_content = "This is the content of the transcript."
    transcript = Transcript(transcript_content)

    interview = Interview(interviewee, transcript)

    interview.transcribe()

    print(f"Interview Status: {interview.status}")
