from Factories.Creator import DefaultCreator, RandomCreator, OreCreator, ProductCreator
from Factories.Product import *
from Factories.Model import Material

if __name__ == '__main__':

    factory = DefaultCreator(product=IronPlate())
    factory.list_materials()
    print(f'DefaultCreator produce : {factory.produce()}')

    factory.update_material(material=Material(require=IronOre(), amount=10))
    factory.list_materials()
    print(f'DefaultCreator produce after update materials : {factory.produce()}')
    print(f'{"-" * 20}\n')

    random_factory = RandomCreator()
    print(f'RandomCreator produce : {random_factory.produce()}')
    print(f'RandomCreator produce : {random_factory.produce()}')
    print(f'RandomCreator produce : {random_factory.produce()}')
    print(f'RandomCreator produce : {random_factory.produce()}')
    print(f'RandomCreator produce : {random_factory.produce()}')
    print(f'{"-" * 20}\n')

    ore_factory = OreCreator()
    print(f'OreCreator produce : {ore_factory.produce()}')
    print(f'OreCreator produce : {ore_factory.produce()}')
    print(f'OreCreator produce : {ore_factory.produce()}')
    print(f'{"-" * 20}\n')

    product_factory = ProductCreator()
    print(f'ProductCreator produce : {product_factory.produce()}')
    print(f'ProductCreator produce : {product_factory.produce()}')
    print(f'ProductCreator produce : {product_factory.produce()}')
    print(f'{"-" * 20}\n')

    factories = [
        factory, random_factory, ore_factory, product_factory
    ]

    for fact in factories:
        print(f'{fact.__class__.__name__} get {fact.product.name} description {fact.product.get_description()}')
