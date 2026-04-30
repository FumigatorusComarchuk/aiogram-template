from dataclasses import dataclass


@dataclass(slots=True)
class Message:
    text: str
