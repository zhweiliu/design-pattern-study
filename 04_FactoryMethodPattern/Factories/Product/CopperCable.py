from .Product import Product, DescriptionData
from ..Model import Material
from .CopperOre import CopperOre


class CopperCable(Product):

    @property
    def name(self) -> str:
        return 'copper cable'

    def get_description(self) -> DescriptionData:
        return DescriptionData(
            materials=[
                Material(require=CopperOre(), amount=1),
            ],
            name=self.name,
            output=3
        )
