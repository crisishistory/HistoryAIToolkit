from enum import StrEnum, auto
from pydantic import BaseModel, NonNegativeInt

class Gender(StrEnum):
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()


class Interviewee(BaseModel):
    """An Interviewee is a person who is interviewed."""

    name: str
    age: NonNegativeInt
    gender: Gender