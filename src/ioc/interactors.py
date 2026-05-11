from dishka import Provider, Scope, provide

from src.application.interactors import StartInteractor, GetNumberOfUsersInteractor


class InteractorsProvider(Provider):
    start_interactor = provide(StartInteractor, scope=Scope.REQUEST)
    get_number_of_users_interactor = provide(
        GetNumberOfUsersInteractor, scope=Scope.REQUEST
    )
