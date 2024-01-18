class Cocktail:
    def __init__(self, id, alcoholic, drink, glass, ingredients, ingredients_and_quantities, instructions, sour, sweet, cream, bitter, water, herbal, egg, salty, spicy):
        self.id = id
        self.alcoholic = alcoholic
        self.drink = drink
        self.glass = glass
        self.ingredients = ingredients
        self.ingredients_and_quantities = ingredients_and_quantities
        self.instructions = instructions
        self.sour = sour
        self.sweet = sweet
        self.cream = cream
        self.bitter = bitter
        self.water = water
        self.herbal = herbal
        self.egg = egg
        self.salty = salty
        self.spicy = spicy
        
    def __str__(self):
        return f"Cocktail(id={self.id}, alcoholic={self.alcoholic}, drink={self.drink}, glass={self.glass}, ingredients={self.ingredients}, ingredients_and_quantities={self.ingredients_and_quantities}, instructions={self.instructions}, sour={self.sour}, sweet={self.sweet}, cream={self.cream}, bitter={self.bitter}, water={self.water}, herbal={self.herbal}, egg={self.egg}, salty={self.salty}, spicy={self.spicy})"