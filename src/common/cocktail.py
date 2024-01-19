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
        
        
    def get_positive_tastes(self, max_length=3):
        result = []
        if self.sour:
            result.append("sour")
        if self.sweet:
            result.append("sweet")
        if self.cream:
            result.append("cream")
        if self.bitter:
            result.append("bitter")
        if self.water:
            result.append("water")
        if self.herbal:
            result.append("herbal")
        if self.egg:
            result.append("egg")
        if self.salty:
            result.append("salty")
        if self.spicy:
            result.append("spicy")
        return result[:max_length]
    
    
    def __str__(self):
        return f"Cocktail(id={self.id}, alcoholic={self.alcoholic}, drink={self.drink}, glass={self.glass}, ingredients={self.ingredients}, ingredients_and_quantities={self.ingredients_and_quantities}, instructions={self.instructions}, sour={self.sour}, sweet={self.sweet}, cream={self.cream}, bitter={self.bitter}, water={self.water}, herbal={self.herbal}, egg={self.egg}, salty={self.salty}, spicy={self.spicy})"