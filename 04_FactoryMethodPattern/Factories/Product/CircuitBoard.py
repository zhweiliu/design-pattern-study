from .Product import Product, DescriptionData
from ..Model import Material

from .IronPlate import IronPlate
from .CopperCable import CopperCable


class CircuitBoard(Product):
    @property
    def name(self) -> str:
        return 'circuit board'

    def get_description(self) -> DescriptionData:
        return DescriptionData(
            materials=[
                Material(require=IronPlate(), amount=1),
                Material(require=CopperCable(), amount=2)
            ],
            name=self.name,
            output=1
        )
