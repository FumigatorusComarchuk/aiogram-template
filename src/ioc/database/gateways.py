from dishka import Provider, Scope, provide, AnyOf

from src.application.interfaces import (
    IUserSaver,
    IUserGetter,
    IUserAccountGetter,
    IUserAccountSaver,
    IUserAccountGateway,
)
from src.adapters.infrastructure.database.gateways import (
    UserGatewayImpl,
    UserAccountGatewayImpl,
)


class DatabaseGatewaysProvider(Provider):
    user_gateway = provide(
        UserGatewayImpl, scope=Scope.REQUEST, provides=AnyOf[IUserSaver, IUserGetter]
    )
    user_account = provide(
        UserAccountGatewayImpl,
        scope=Scope.REQUEST,
        provides=AnyOf[IUserAccountGetter,
                       IUserAccountSaver, IUserAccountGateway],
    )
