from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: float | int = 0
