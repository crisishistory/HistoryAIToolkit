from enum import StrEnum, auto


class Gender(StrEnum):
    MALE = auto()
    FEMALE = auto()
    OTHER = auto()


class Interviewee:
    """An Interviewee is a person who is interviewed."""

    def __init__(self, name: str, age: int, gender: Gender):
        self.name = name
        self.age = age
        self.gender = gender
