from .Product import Product, DescriptionData


class CopperOre(Product):
    @property
    def name(self) -> str:
        return 'copper ore'

    def get_description(self) -> DescriptionData:
        return DescriptionData(
            materials=[],
            name=self.name,
            output=1
        )
