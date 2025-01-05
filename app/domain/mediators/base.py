import abc
from abc import abstractmethod
from typing import TypeVar

T = TypeVar('T')
R = TypeVar('R')


class BaseMediator(abc.ABC):

    @abstractmethod
    async def handle(self, query: T) -> R:
        ...

    @abstractmethod
    def bind(self, query: T, handler: object) -> None:
        ...