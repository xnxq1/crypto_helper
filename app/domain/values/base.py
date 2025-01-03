import abc
from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class ValueObject[T](abc.ABC):
    value: T

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self) -> None: ...

    def to_raw(self) -> T:
        return self.value
