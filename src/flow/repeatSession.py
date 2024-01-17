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
    
    last_drink = user_data[5]
    common.say(furhat, f"I remember that I gave you {last_drink} last time. Would you like to a different drink?")
    
    # Wait for the user's response
    user_response = common.user_response(furhat)

    # Sentiment analysis on response
    if sentiment_analysis.query(user_response.message) == "POSITIVE":
        # Go to recommendCocktails
        recommendCocktails.run(furhat)
        return
    else:
        buildModel.run(furhat, user_data)
        return
