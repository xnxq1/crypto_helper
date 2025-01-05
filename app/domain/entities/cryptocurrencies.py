from dataclasses import dataclass

from app.domain.values.cryptocurrencies import CryptoAbbreviation


@dataclass
class CryptoPrice:
    crypto: CryptoAbbreviation
    quantity: float

    def get_price(self, price: float) -> float:
        return self.quantity * price
