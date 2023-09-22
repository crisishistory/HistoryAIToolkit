class Interview(object):
    """An interview between an Interviewee and an Interviewer."""
    
    def __init__(self, interviewee, transcript):
        self.interviewee = interviewee
        self.transcript = transcript
        self.status = "Not Transcribed"  # Initial status

    def transcribe(self):
        self.status = "Transcribed"
