from dishka import Provider, Scope, provide

from src.application.interactors import (
    StartInteractor,
)


class InteractorsProvider(Provider):
    start_interactor = provide(StartInteractor, scope=Scope.REQUEST)
