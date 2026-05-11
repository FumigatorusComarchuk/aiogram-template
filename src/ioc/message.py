from dishka import Provider, Scope, provide

from src.application.interfaces import IMessageGateway
from src.adapters.infrastructure.message import MessageGateway


class MessageGatewayProvider(Provider):
    message_gateway = provide(
        MessageGateway, scope=Scope.REQUEST, provides=IMessageGateway
    )
