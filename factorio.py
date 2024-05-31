class Recipe:
    def __init__(self, name, inputs, output_quantity=1):
        self.name = name
        self.inputs = inputs
        self.output_quantity = output_quantity

recipes = []

recipes.append(Recipe("iron plate", [("iron ore", 1)]))
recipes.append(Recipe("iron gear", [("iron plate", 2)]))
recipes.append(Recipe("iron stick", [("iron plate", 1)], 2))


print(recipes)
