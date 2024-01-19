import random
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database


def run(furhat: FurhatRemoteAPI, cocktail, user):
    print("Recommended cocktail: ", cocktail)
    user.last_drink = cocktail.drink
    user.sour = cocktail.sour
    user.sweet = cocktail.sweet
    user.cream = cocktail.cream
    user.bitter = cocktail.bitter
    user.water = cocktail.water
    user.herbal = cocktail.herbal
    user.egg = cocktail.egg
    user.salty = cocktail.salty
    user.spicy = cocktail.spicy
    database.update_user_data(user.id, user)
    phrases = [
        f"Great! Here are the ingredients and instructions for {cocktail.drink}.",
        f"Awesome! Let me provide you with the ingredients and the preparation steps for {cocktail.drink}.",
        f"Excellent! I'll now share the ingredients and how-to guide for making {cocktail.drink}.",
        f"Wonderful! Here's what you'll need and the instructions to create {cocktail.drink}.",
        f"Fantastic! I have the list of ingredients and the method for preparing {cocktail.drink} ready for you.",
    ]
    selected_phrase = random.choice(phrases)
    common.say(furhat, selected_phrase)
    common.say(furhat, cocktail.ingredients_and_quantities)
    common.say(furhat, cocktail.instructions)