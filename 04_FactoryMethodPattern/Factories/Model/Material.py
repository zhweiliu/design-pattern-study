from typing import NamedTuple
from ..Product import IProduct


class Material(NamedTuple):
    require: IProduct
    amount: float

    def __repr__(self) -> str:
        return self.require.name
