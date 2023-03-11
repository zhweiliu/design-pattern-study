from .Product import Product
from .Meat import Meat


class Burger(Product):
    def __init__(self, meat: Meat, meat_piece: int):
        self.vegetables: list[str] = ['lettuce', 'tomato', 'pickles']
        self._meat: Meat = meat
        self._meat_piece: int = meat_piece

    @property
    def name(self) -> str:
        return f'{self._meat.name} burger'

    @property
    def meat_piece(self) -> int:
        return self._meat_piece

    @property
    def bread_price(self) -> float:
        return 20.0

    @property
    def price(self) -> float:
        return self.bread_price + (self.meat_piece * self._meat.price)

    def get_description(self) -> dict:
        return {
            'name': self.name,
            'price': self.price,
            'ingredient': {
                'meat': f'{self._meat} x {self.meat_piece}',
                'vegetables': self.vegetables
            }
        }


