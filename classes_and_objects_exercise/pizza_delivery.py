class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered: bool = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> [None, str]:
        if not self.ordered:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity

            else:
                self.ingredients[ingredient] = quantity

            self.price += quantity * price_per_quantity

        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> [str, None]:
        if not self.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"

            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self) -> str:
        if not self.ordered:
            self.ordered = True
            result = []
            for k, v in self.ingredients.items():
                result.append(f"{k}: {v}")

            return f"You've ordered pizza {self.name} prepared with {', '.join(result)} and the price will be {self.price}lv."

        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

