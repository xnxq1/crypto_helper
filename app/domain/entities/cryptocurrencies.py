from dataclasses import dataclass

from app.domain.values.cryptocurrencies import CryptoAbbreviation


class CryptoPair:
    first_crypto: CryptoAbbreviation
    second_crypto: CryptoAbbreviation
    price: float


    def to_raw(self) -> str:
        return self.first_crypto.to_raw() + '/' + self.second_crypto.to_raw()