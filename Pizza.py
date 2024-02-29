class Pizza:
    def PepperoniPizza(name, )


class Order():
    """
     Class program
    """
    def __init__(self) -> None:
        self.pizzas: list[Pizza] = []

    def add_pizza(self, pizza:Pizza) -> None:
        """ добавляет пиццу"""
        self.pizzas.append(pizza)

    def calculate_total(self) -> int:
        """ возврашает"""
        return sum(pizza.prise)