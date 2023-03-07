from typing import Union
from .ICreator import ICreator, IProduct, Material
from ..Product import IronPlate, CopperCable

import random


class ProductCreator(ICreator):
    def __init__(self):
        super().__init__(None)

    def produce(self) -> Union[IProduct, None]:
        product_list = [IronPlate, CopperCable]

        self.product = product_list[random.randrange(len(product_list))]()
        return self.product


