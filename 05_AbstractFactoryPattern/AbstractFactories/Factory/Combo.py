from abc import ABC, abstractmethod

from ..Product import Burger, Drink, Fries, DrinkSize, DrinkSizeEnum, DrinkSizePriceEnum
from ..Creator import BeefBurgerCreator, PorkBurgerCreator, CokeCreator, SupersizeFriesCreator, MediumFriesCreator, \
    FishBurgerCreator, GreenTeaCreator


class Combo(ABC):

    @abstractmethod
    def get_burger(self) -> Burger:
        pass

    @abstractmethod
    def get_drink(self) -> Drink:
        pass

    @abstractmethod
    def get_fries(self) -> Fries:
        pass


class PorkBurgerCombo(Combo):
    def get_burger(self) -> Burger:
        return PorkBurgerCreator().get_burger()

    def get_drink(self) -> Drink:
        return CokeCreator(size=DrinkSize(size=DrinkSizeEnum.TALL, price=DrinkSizePriceEnum.TALL)).get_drink()

    def get_fries(self) -> Fries:
        return MediumFriesCreator().get_fries()


class FishBurgerCombo(Combo):

    def get_burger(self) -> Burger:
        return FishBurgerCreator().get_burger()

    def get_drink(self) -> Drink:
        return GreenTeaCreator(size=DrinkSize(size=DrinkSizeEnum.TALL, price=DrinkSizePriceEnum.TALL)).get_drink()

    def get_fries(self) -> Fries:
        return MediumFriesCreator().get_fries()


class SupersizeHamburgerCombo(Combo):
    def get_burger(self) -> Burger:
        return BeefBurgerCreator(meat_piece=4).get_burger()

    def get_drink(self) -> Drink:
        return CokeCreator(size=DrinkSize(size=DrinkSizeEnum.VENTI, price=DrinkSizePriceEnum.VENTI)).get_drink()

    def get_fries(self) -> Fries:
        return SupersizeFriesCreator().get_fries()
