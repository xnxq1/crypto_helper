from functools import lru_cache

from punq import Container

from app.application.app import App


@lru_cache(1)
def create_di():
    container = Container()
    container.register(App, App)

    return container