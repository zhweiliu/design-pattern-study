from abc import ABC, abstractmethod
from ..Product import Fries, FriesSize, FriesSizeEnum, FriesSizePriceEnum


class FriesCreator(ABC):
    @abstractmethod
    def get_fries(self) -> Fries:
        pass


class SupersizeFriesCreator(FriesCreator):

    def get_fries(self) -> Fries:
        return Fries(fries_size=FriesSize(size=FriesSizeEnum.SUPER, price=FriesSizePriceEnum.SUPER))


class LargeFriesCreator(FriesCreator):
    def get_fries(self) -> Fries:
        return Fries(fries_size=FriesSize(size=FriesSizeEnum.LARGE, price=FriesSizePriceEnum.LARGE))


class MediumFriesCreator(FriesCreator):

    def get_fries(self) -> Fries:
        return Fries(fries_size=FriesSize(size=FriesSizeEnum.MEDIUM, price=FriesSizePriceEnum.MEDIUM))
