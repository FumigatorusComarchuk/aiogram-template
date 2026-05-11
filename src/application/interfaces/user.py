from abc import abstractmethod
from typing import Protocol

from src.domain.user import User


class UserSaver(Protocol):
    @abstractmethod
    def save(self, user: User) -> None: ...


class UserGetter(Protocol):
    @abstractmethod
    async def get_by_uuid(self, uuid: str) -> None | User: ...
