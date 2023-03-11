from enum import Enum, StrEnum
from typing import NamedTuple
from .Product import Product


class FriesSizeEnum(StrEnum):
    SUPER = 'super'
    LARGE = 'large'
    MEDIUM = 'medium'


class FriesSizePriceEnum(float, Enum):
    SUPER = 10.0
    LARGE = 7.5
    MEDIUM = 5.0


class FriesSize(NamedTuple):
    size: FriesSizeEnum
    price: FriesSizePriceEnum


class Fries(Product):

    def __init__(self, fries_size: FriesSize):
        self._fries_size: FriesSize = fries_size

    def get_description(self) -> dict:
        return {
            'name': self.name,
            'size': self.size,
            'price': self.price
        }

    @property
    def name(self) -> str:
        return 'fries'

    @property
    def size(self) -> str:
        return str(self._fries_size.size.value)

    @property
    def price(self) -> float:
        return float(self._fries_size.price.value)
