from dataclasses import dataclass

from app.domain.values.cryptocurrencies import CryptoAbbreviation


@dataclass
class CryptoPair:
    first_crypto: CryptoAbbreviation
    second_crypto: CryptoAbbreviation
    price: float

    def __str__(self) -> str:
        return self.first_crypto.to_raw() + "/" + self.second_crypto.to_raw()
