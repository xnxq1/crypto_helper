from app.domain.values.base import ValueObject
from dataclasses import dataclass


@dataclass
class CryptoAbbreviation[str](ValueObject):
    value: str

    def validate(self) -> None:
        self.value = self.value.upper()

    def to_raw(self) -> str:
        return self.value
