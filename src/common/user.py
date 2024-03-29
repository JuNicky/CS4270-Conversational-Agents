class User:
    def __init__(self, id, name, age=None, last_drink=None, occasion=None,
                 sour=False, sweet=False, cream=False, bitter=False, water=False, herbal=False, egg=False, salty=False, spicy=False):
        self.id = id
        self.name = name
        self.age = age
        self.last_drink = last_drink
        self.occasion = occasion
        self.sour = sour
        self.sweet = sweet
        self.cream = cream
        self.bitter = bitter
        self.water = water
        self.herbal = herbal
        self.egg = egg
        self.salty = salty
        self.spicy = spicy

    def set_age(self, age):
        self.age = age

    def set_last_drink(self, last_drink):
        self.last_drink = last_drink

    def set_occasion(self, occasion):
        self.occasion = occasion
    
    def set_sour(self, sour):
        self.sour = sour
    
    def set_cream(self, cream):
        self.cream = cream
    
    def set_bitter(self, bitter):
        self.bitter = bitter
    
    def set_water(self, water):
        self.water = water

    def set_herbal(self, herbal):
        self.herbal = herbal
    
    def set_egg(self, egg):
        self.egg = egg
    
    def set_salty(self, salty):
        self.salty = salty
    
    def set_spicy(self, spicy):
        self.spicy = spicy
    
    def __str__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age}, last_drink={self.last_drink}, occasion={self.occasion}, sour={self.sour}, sweet={self.sweet}, cream={self.cream}, bitter={self.bitter}, water={self.water}, herbal={self.herbal}, egg={self.egg}, salty={self.salty}, spicy={self.spicy})"