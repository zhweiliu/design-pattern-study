from typing import Union

from .ICreator import ICreator, IProduct, Material


class DefaultCreator(ICreator):
    """
    DefaultCreator will provide a product at once.
    """

    def produce(self) -> Union[IProduct, None]:
        product_description = self.product.get_description()
        require_materials: list[Material] = product_description.materials

        material_to_product = {}

        # calculate the maximum of can produce of each material by floor divide
        for m in require_materials:
            if not self.check_material(m.require.name):
                return None

            material_to_product[m.require.name] = self.materials[m.require.name] // m.amount

        product = self.product if min(material_to_product.values()) > 0 else None

        return product
