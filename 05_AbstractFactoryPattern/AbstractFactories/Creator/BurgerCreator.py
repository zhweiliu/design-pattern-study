from abc import ABC, abstractmethod
from ..Product import Burger, Beef, Pork, Fish


class BurgerCreator(ABC):

    def __init__(self, meat_piece: int = 1):
        self._meat_piece = meat_piece

    @abstractmethod
    def get_burger(self) -> Burger:
        pass


class BeefBurgerCreator(BurgerCreator):
    def get_burger(self) -> Burger:
        return Burger(meat=Beef(), meat_piece=self._meat_piece)


class PorkBurgerCreator(BurgerCreator):

    def get_burger(self) -> Burger:
        return Burger(meat=Pork(), meat_piece=self._meat_piece)


class FishBurgerCreator(BurgerCreator):

    def get_burger(self) -> Burger:
        return Burger(meat=Fish(), meat_piece=self._meat_piece)
