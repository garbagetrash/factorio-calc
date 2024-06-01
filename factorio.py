#!/usr/bin/env python3

class Recipe:
    def __init__(self, name, inputs, output_quantity=1):
        self.name = name
        self.inputs = inputs
        self.output_quantity = output_quantity

    def __repr__(self):
        return f"{self.output_quantity} {self.name}: {self.inputs}"

def basic_materials(recipe):
    for ingredient, quantity in recipe.inputs:
        pass

recipes = {}

recipes["copper plate"] = Recipe("copper plate", [("copper ore", 1)])
recipes["copper cable"] = Recipe("copper cable", [("copper plate", 1)], 2)
recipes["iron plate"] = Recipe("iron plate", [("iron ore", 1)])
recipes["iron gear"] = Recipe("iron gear", [("iron plate", 2)])
recipes["iron stick"] = Recipe("iron stick", [("iron plate", 1)], 2)
recipes["single cylinder engine"] = Recipe("single cylinder engine", [
    ("iron gear", 1),
    ("iron plate", 1),
    ])
recipes["small electric motor"] = Recipe("small electric motor", [
    ("iron gear", 1),
    ("copper cable", 6),
    ("iron plate", 1),
    ])
recipes["burner inserter"] = Recipe("burner inserter", [
    ("iron stick", 2),
    ("single cylinder engine", 1),
    ])
recipes["inserter"] = Recipe("inserter", [
    ("burner inserter", 1),
    ("small electric motor", 1),
    ])
recipes["yellow belt"] = Recipe("yellow belt", [
    ("single cylinder engine", 1),
    ("iron plate", 1),
    ], 2)
recipes["yellow underground belt"] = Recipe("yellow underground belt", [
    ("yellow belt", 5),
    ("iron plate", 10),
    ], 2)
recipes["yellow splitter"] = Recipe("yellow splitter", [
    ("single cylinder engine", 4),
    ("yellow belt", 4),
    ("iron plate", 8),
    ])


for recipe in recipes.values():
    print(recipe)
