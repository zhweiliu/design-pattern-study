from abc import ABCMeta, abstractmethod
from .Product import Product


class Meat(Product, metaclass=ABCMeta):

    def get_description(self) -> dict:
        return {
            'name': self.name,
            'price': self.price
        }


class Beef(Meat):

    @property
    def name(self) -> str:
        return 'beef'

    @property
    def price(self) -> float:
        return 30.0


class Pork(Meat):

    @property
    def name(self) -> str:
        return 'pork'

    @property
    def price(self) -> float:
        return 25.0


class Fish(Meat):

    @property
    def name(self) -> str:
        return 'fish'

    @property
    def price(self) -> float:
        return 20.0
