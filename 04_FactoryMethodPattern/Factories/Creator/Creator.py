from abc import ABCMeta, abstractmethod
from ..Product import Product
from ..Model import Material
from typing import Union


class Creator(metaclass=ABCMeta):

    def __init__(self, product: Union[Product, None]):
        super().__init__()
        # assign a specific product for creator
        self.product: Product = product

        # initialize the materials list,
        # use dictionary for unique each material
        self.materials: dict = {}

    def update_material(self, material: Material):
        # update the stock amount for material to materials list
        amount = material.amount
        if material.require.name in self.materials:
            amount += self.materials[material.require.name]

        self.materials[material.require.name] = amount

    def list_materials(self):
        print(f'{self.__class__.__name__} materials : {self.materials}')

    def check_material(self, require: str) -> Union[Material, None]:
        result = None
        if require in self.materials:
            result = self.materials[require]

        return result

    @abstractmethod
    def produce(self) -> Union[Product, None]:
        pass
