from furhat_remote_api import FurhatRemoteAPI
from src.common import database
from src.flow import recommendCocktails


# Asks the user questions and builds a model of the user.
def run(furhat: FurhatRemoteAPI, user_id, user):
    print("We are currently running buildModel.py")
    recommendCocktails.run(furhat, user_id, user)
    # Ask questions and to build model
    # Suggestions on how to do it: make a GPT model
    # When the model is created, save to database
    # Go to recommendCocktails.py
    pass
