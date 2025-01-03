from functools import lru_cache

from punq import Container


from app.config import Config


@lru_cache(1)
def init_container():
    container = Container()
    container.register(Config, instance=Config())

    return container
