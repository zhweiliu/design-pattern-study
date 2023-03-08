from typing import Union
from .Creator import Creator, Product, Material
from ..Product import IronOre, CopperOre

import random


class OreCreator(Creator):
    def __init__(self):
        super().__init__(None)

    def produce(self) -> Union[Product, None]:
        ore_list = [IronOre, CopperOre]

        self.product = ore_list[random.randrange(len(ore_list))]()

        return self.product


