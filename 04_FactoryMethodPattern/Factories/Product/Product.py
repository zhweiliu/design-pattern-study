from abc import ABCMeta, abstractmethod
from typing import Any

from ..Model import DescriptionData


class Product(metaclass=ABCMeta):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    def __repr__(self):
        return self.name

    @abstractmethod
    def get_description(self) -> DescriptionData:
        pass
