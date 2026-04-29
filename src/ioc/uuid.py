from uuid import uuid4

from dishka import Provider, Scope, provide

from src.application.interfaces import UUIDGenerator


class UUIDProvider(Provider):
    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> UUIDGenerator:
        return uuid4
