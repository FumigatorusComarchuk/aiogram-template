from dataclasses import dataclass
from .from_user import FromUserDTO


@dataclass(slots=True)
class GetNumberOfUsersRequestDTO:
    platform: str
    from_user: FromUserDTO


@dataclass(slots=True)
class GetNumberOfUsersResponseDTO:
    text: str
