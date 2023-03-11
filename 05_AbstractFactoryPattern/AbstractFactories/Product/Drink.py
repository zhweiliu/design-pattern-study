from abc import ABCMeta, abstractmethod
from enum import Enum, StrEnum
from typing import NamedTuple
from .Product import Product


class DrinkSizeEnum(StrEnum):
    VENTI = 'venti'
    GRANDE = 'grande'
    TALL = 'tall'
    SHORT = 'short'


class DrinkSizePriceEnum(float, Enum):
    VENTI = 10.0
    GRANDE = 7.5
    TALL = 5.0
    SHORT = 2.5


class DrinkSize(NamedTuple):
    size: DrinkSizeEnum
    price: DrinkSizePriceEnum


class Drink(Product, metaclass=ABCMeta):

    def __init__(self, drink_size: DrinkSize):
        self._drink_size: DrinkSize = drink_size

    @property
    def size(self) -> str:
        return str(self._drink_size.size.value)

    @property
    def price(self) -> float:
        return float(self._drink_size.price.value)

    def get_description(self) -> dict:
        return {
            'name': self.name,
            'size': self.size,
            'price': self.price
        }


class Coke(Drink):

    @property
    def name(self) -> str:
        return 'coke'


class Soda(Drink):

    @property
    def name(self) -> str:
        return 'soda'


class GreenTea(Drink):

    @property
    def name(self) -> str:
        return 'green tea'
