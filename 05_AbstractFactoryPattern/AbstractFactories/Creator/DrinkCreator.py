from abc import ABC, abstractmethod
from ..Product import Drink, Coke, Soda, GreenTea, DrinkSize


class DrinkCreator(ABC):

    def __init__(self, size: DrinkSize):
        self._size: DrinkSize = size

    @abstractmethod
    def get_drink(self) -> Drink:
        pass


class CokeCreator(DrinkCreator):

    def get_drink(self) -> Drink:
        return Coke(drink_size=self._size)


class SodaCreator(DrinkCreator):

    def get_drink(self) -> Drink:
        return Soda(drink_size=self._size)


class GreenTeaCreator(DrinkCreator):
    def get_drink(self) -> Drink:
        return GreenTea(drink_size=self._size)
