from typing import Union
from .ICreator import ICreator, IProduct, Material
from ..Product import IronOre, CopperOre

import random


class OreCreator(ICreator):
    def __init__(self):
        super().__init__(None)

    def produce(self) -> Union[IProduct, None]:
        ore_list = [IronOre, CopperOre]

        self.product = ore_list[random.randrange(len(ore_list))]()

        return self.product


