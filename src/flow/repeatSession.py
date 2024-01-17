from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
from src.experiments import cosine_similarity, sentiment_analysis
from src.flow import buildModel, recommendCocktails

# We only reach this function once it's at least the 2nd time encountering the user
def run(furhat: FurhatRemoteAPI, user_data):
    print("We are currently running repeatSession.py") 
    # If the user wants to change their recipe
        # Go to buildModel
    # Else
        # Go to recommend cocktails
    
    last_drink = user_data.last_drink
    common.say(furhat, f"I remember that I gave you {last_drink} last time. Would you like the same drink?")
    
    # Wait for the user's response
    user_response = common.user_response(furhat)

    # Sentiment analysis on response
    if sentiment_analysis.query(user_response.message) == "NEGATIVE":
        # Go to recommendCocktails
        recommendCocktails.run(furhat, user_data.user_id, user_data)
        return
    else:
        cocktail = database.get_drink_by_cocktail(last_drink)

        print(cocktail)
        common.say(furhat, f"Here are the ingredients and instructions for {last_drink}.")
        common.say(furhat, cocktail.ingredients_and_quantities)
        common.say(furhat, cocktail.instructions)
        return
