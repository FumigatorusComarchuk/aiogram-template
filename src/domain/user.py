from enum import StrEnum
from dataclasses import dataclass


class UserRole(StrEnum):
    MAIN_ADMIN = "main_admin"
    USER = "user"


@dataclass(slots=True)
class User:
    uuid: str
    role: UserRole
