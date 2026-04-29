from dataclasses import dataclass


@dataclass(slots=True)
class StartRequestDTO:
    platform: str | None
    platform_user_id: str | None


@dataclass(slots=True)
class StartResponseDTO:
    text: str
