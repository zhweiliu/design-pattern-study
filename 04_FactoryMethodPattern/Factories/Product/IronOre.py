from .IProduct import IProduct, DescriptionData


class IronOre(IProduct):
    @property
    def name(self) -> str:
        return 'iron ore'

    def get_description(self) -> DescriptionData:
        return DescriptionData(
            materials=[],
            name=self.name,
            output=1
        )
