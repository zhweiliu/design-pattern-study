from typing import Union
from .Creator import Creator, Product, Material
from ..Product import IronPlate, CopperCable

import random


class ProductCreator(Creator):
    def __init__(self):
        super().__init__(None)

    def produce(self) -> Union[Product, None]:
        product_list = [IronPlate, CopperCable]

        self.product = product_list[random.randrange(len(product_list))]()
        return self.product


