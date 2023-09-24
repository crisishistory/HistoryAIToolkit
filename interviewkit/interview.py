from random import choice

import openai



class Interview(object):
    """An interview between an Interviewee and an Interviewer."""
    
    def __init__(self, interviewee):
        self.interviewee = interviewee
        self.status = "In Progress"

    def start_recording(self):
        """ Start recording audio. """
        self.status = "Recording"

    def stop_recording(self):
        """ Stop recording audio. """
        self.status = "Recorded"

    def start_transcription(self):
        self.status = "Transcribing"
        self.transcript = []

    def add_to_transcript(self, speech):
        self.transcript.append(speech)

    def stop_transcription(self):
        self.status = "Transcribed"

        # Combine list of transcribed text into a single string
        self.transcript = ' '.join(self.transcript)

    def suggest_questions(self):
        """ Use the OpenAI API to suggest questions based on the transcript content. """
        suggested_questions = self.generate_questions(self.transcript)
        return suggested_questions

    def generate_questions(self, content):
        """ Call the OpenAI API to generate questions, and return them. """
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate interview questions based on the following transcript:\n{content}\n",
            max_tokens=50,  # Adjust the max tokens as needed
            n=5,  # Number of questions to generate
            stop=None,
            temperature=0.7  # Adjust the temperature for creativity
        )

        # Extract and return the generated questions
        generated_questions = [choice['text'].strip() for choice in response.choices]
        return generated_questions
