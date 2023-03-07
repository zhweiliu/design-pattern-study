from typing import Union
from .ICreator import ICreator, IProduct, Material
from ..Product import *

import random


class RandomCreator(ICreator):
    """
    RandomCreator will provide a random product directly.
    """

    def __init__(self):
        super().__init__(None)

    def produce(self) -> Union[IProduct, None]:
        product_list = [
            IronOre, CopperOre, IronPlate, CopperCable, CircuitBoard
        ]

        self.product = product_list[random.randrange(len(product_list))]()

        return self.product
