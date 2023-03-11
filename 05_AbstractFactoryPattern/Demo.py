from AbstractFactories.Factory.Combo import Combo, PorkBurgerCombo, FishBurgerCombo, SupersizeHamburgerCombo


def order_information(combo: Combo):
    burger = combo.get_burger()
    drink = combo.get_drink()
    fries = combo.get_fries()

    description = {
        'burger': burger.get_description(),
        'drink': drink.get_description(),
        'fries': fries.get_description(),
        'total_price': burger.price + drink.price + fries.price
    }

    print(f'Combo: {combo.__class__.__name__}')
    print(description)
    print('-' * 30)


if __name__ == '__main__':
    pork_combo = PorkBurgerCombo()
    order_information(pork_combo)

    fish_combo = FishBurgerCombo()
    order_information(fish_combo)

    hamburger_combo = SupersizeHamburgerCombo()
    order_information(hamburger_combo)
