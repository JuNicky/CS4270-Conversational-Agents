class User:
    def __init__(self, id, name, age=None, visit=None, last_drink=None, occasion=None,
                 sweet=False, sour=False, spicy=False, bitter=False,
                 fruity=False, savory=False, hot=False, frozen=False, refreshing=False):
        self.id = id
        self.name = name
        self.age = age
        self.visit = visit
        self.last_drink = last_drink
        self.occasion = occasion
        self.sweet = sweet
        self.sour = sour
        self.spicy = spicy
        self.bitter = bitter
        self.fruity = fruity
        self.savory = savory
        self.hot = hot
        self.frozen = frozen
        self.refreshing = refreshing

    def set_age(self, age):
        self.age = age

    def set_visit(self, visit):
        self.visit = visit

    def set_last_drink(self, last_drink):
        self.last_drink = last_drink

    def set_occasion(self, occasion):
        self.occasion = occasion

    def set_sweet(self, sweet):
        self.sweet = sweet

    def set_sour(self, sour):
        self.sour = sour

    def set_spicy(self, spicy):
        self.spicy = spicy

    def set_bitter(self, bitter):
        self.bitter = bitter

    def set_fruity(self, fruity):
        self.fruity = fruity

    def set_savory(self, savory):
        self.savory = savory

    def set_hot(self, hot):
        self.hot = hot

    def set_frozen(self, frozen):
        self.frozen = frozen

    def set_refreshing(self, refreshing):
        self.refreshing = refreshing
    
    def set_last_drink(self, last_drink):
        self.last_drink = last_drink
    
    def set_sour(self, sour):
        self.sour = sour
    
    def set_spicy(self, spicy):
        self.spicy = spicy
    
    def set_bitter(self, bitter):
        self.bitter = bitter
    
    def set_fruity(self, fruity):
        self.fruity = fruity
    
    def set_savory(self, savory):
        self.savory = savory
    
    def set_hot(self, hot):
        self.hot = hot
    
    def set_frozen(self, frozen):
        self.frozen = frozen
    
    def set_refreshing(self, refreshing):
        self.refreshing = refreshing
    
    def __str__(self):
        return f"User(name={self.name}, age={self.age}, visit={self.visit}, last_drink={self.last_drink}, occasion={self.occasion}, sweet={self.sweet}, sour={self.sour}, spicy={self.spicy}, bitter={self.bitter}, fruity={self.fruity}, savory={self.savory}, hot={self.hot}, frozen={self.frozen}, refreshing={self.refreshing})"