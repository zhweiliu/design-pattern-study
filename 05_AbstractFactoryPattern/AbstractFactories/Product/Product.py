from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    def __repr__(self):
        return self.name

    @abstractmethod
    def get_description(self) -> dict:
        pass
