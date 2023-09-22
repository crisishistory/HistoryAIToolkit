import os

from dotenv import load_dotenv
import openai

from interview import Interview
from interviewee import Interviewee
from transcript import Transcript


# Load the .env file into the environment
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":

    interviewee = Interviewee("John Doe", 60, "Male")

    transcript_content = "This is the content of the transcript."
    transcript = Transcript(transcript_content)

    interview = Interview(interviewee, transcript)

    interview.transcribe()

    print(f"Interview Status: {interview.status}")
