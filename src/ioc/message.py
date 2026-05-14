from dishka import Provider, Scope, provide

from src.application.interfaces import IMessageGateway
from src.adapters.infrastructure.message import MessageGatewayImpl


class MessageGatewayProvider(Provider):
    message_gateway = provide(
        MessageGatewayImpl, scope=Scope.REQUEST, provides=IMessageGateway
    )
