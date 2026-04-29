from abc import abstractmethod
from typing import Protocol

from src.domain.user import User


class UserSaver(Protocol):
    @abstractmethod
    def save(self, user: User) -> None: ...
