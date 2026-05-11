from abc import abstractmethod
from typing import Protocol


class IDBSession(Protocol):
    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def flush(self) -> None: ...
