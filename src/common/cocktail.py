class Cocktail:
    def __init__(self, id, alcoholic, drink, glass, ingredients, ingredients_and_quantities, instructions):
        self.id = id
        self.alcoholic = alcoholic
        self.drink = drink
        self.glass = glass
        self.ingredients = ingredients
        self.ingredients_and_quantities = ingredients_and_quantities
        self.instructions = instructions
        
    def __str__(self):
        return f"Cocktail(id={self.id}, alcoholic={self.alcoholic}, drink={self.drink}, glass={self.glass}, ingredients={self.ingredients}, ingredients_and_quantities={self.ingredients_and_quantities}, instructions={self.instructions})"