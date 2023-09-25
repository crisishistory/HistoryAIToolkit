from pydantic import BaseModel


class Transcript(BaseModel):
    """The Transcript entity represents the transcript of an interview."""

    content: str
