from .Product import Product, DescriptionData


class IronOre(Product):
    @property
    def name(self) -> str:
        return 'iron ore'

    def get_description(self) -> DescriptionData:
        return DescriptionData(
            materials=[],
            name=self.name,
            output=1
        )
