from .Product import Product, DescriptionData
from ..Model import Material
from .IronOre import IronOre


class IronPlate(Product):

    @property
    def name(self) -> str:
        return 'iron plate'

    def get_description(self) -> DescriptionData:
        return DescriptionData(
            materials=[
                Material(require=IronOre(), amount=1),
            ],
            name=self.name,
            output=1
        )
