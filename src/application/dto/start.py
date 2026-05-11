from dataclasses import dataclass


@dataclass(slots=True)
class StartRequestDTO:
    platform: str
    platform_user_id: str


@dataclass(slots=True)
class StartResponseDTO:
    text: str
