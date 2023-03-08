from typing import NamedTuple
from ..Product import Product


class Material(NamedTuple):
    require: Product
    amount: float

    def __repr__(self) -> str:
        return self.require.name
