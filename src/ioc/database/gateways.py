from dishka import Provider, Scope, provide, AnyOf

from src.application.interfaces import (
    IUserSaver,
    IUserGetter,
    IUserAccountGetter,
    IUserAccountSaver,
    IUserAccountGateway,
)
from src.adapters.infrastructure.database.gateways import (
    UserGateway,
    UserAccountGateway,
)


class DatabaseGatewaysProvider(Provider):
    user_gateway = provide(
        UserGateway, scope=Scope.REQUEST, provides=AnyOf[IUserSaver, IUserGetter]
    )
    user_account = provide(
        UserAccountGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[IUserAccountGetter,
                       IUserAccountSaver, IUserAccountGateway],
    )
