import time
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
from src.common.api_calls import query
from src.experiments import cosine_similarity, sentiment_analysis
# Recommends cocktails to the user based on their preferences
def run(furhat: FurhatRemoteAPI):
    # Calculate cocktail using cosine similarity
    # Ask if the user wants the cocktail
    # Yes:
        # Update the user's model
        # Provide the recipe
    # No:
        # Ask what the user wants to change
        # Recommend next cocktail
    
    common.say(furhat, "What kind of cocktail would you like?")

    # Wait for the user's response
    # For context, I made a custom function that calls their function.
    # The only thing that is changed, is that when the message is empty, succes should also be false.
    user_response = common.user_response(furhat)
    
    recommended_cocktail, ingredients, instructions, occasion = cosine_similarity.recommend_cocktail(user_response.message)
    

    common.say(furhat, f"For the {occasion} I recommend a {recommended_cocktail} cocktail. Would you like to make it?")
 
    # Wait for the user's response
    user_response = common.user_response(furhat)

    print(query(user_response.message, model='sentiment'))
    # Sentiment analysis on response user later on
    while query(user_response.message, model='sentiment') == "NEGATIVE":
        common.say(furhat, "Oh what can we change about the cocktail?")
        user_response = common.user_response(furhat)
        
        recommended_cocktail, ingredients, instructions = cosine_similarity.recommend_cocktail(user_response.message)
        

        common.say(furhat, "I recommend a " + recommended_cocktail + " cocktail. Would you like to make it?")

        user_response = common.user_response(furhat)
    
    
    common.say(furhat, "Great! Here are the ingredients and instructions.")
    common.say(furhat, ingredients)
    common.say(furhat, instructions)
