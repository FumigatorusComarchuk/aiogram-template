from typing import Protocol
from uuid import UUID


class IUUIDGenerator(Protocol):
    def __call__(self) -> UUID: ...
