from functools import lru_cache

from punq import Container

from app.application.telegram.handlers import Test
from app.application.telegram.mediator import ButtonMediator
from app.settings.config import Config
from app.logic.services.handlers.check_price_handler import PriceCryptoHandler


@lru_cache(1)
def init_container():
    container = Container()
    container.register(Config, instance=Config())
    container.register(PriceCryptoHandler)

    def init_button_mediator():
        mediator = ButtonMediator()
        test = Test()

        mediator.bind('button1', test)
        return mediator

    container.register(ButtonMediator, factory=init_button_mediator)
    return container
