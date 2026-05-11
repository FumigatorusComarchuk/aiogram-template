from dataclasses import dataclass


@dataclass(slots=True)
class FromUserDTO:
    user_id: str
    platform: str
