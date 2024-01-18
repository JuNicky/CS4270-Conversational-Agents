import time
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
from src.common.api_calls import query, get_occasion
from src.experiments import cosine_similarity, sentiment_analysis


# Recommends cocktails to the user based on their preferences
def run(furhat: FurhatRemoteAPI, user_id, user):
    # Calculate cocktail using cosine similarity
    # Ask if the user wants the cocktail
    # Yes:
        # Update the user's model
        # Provide the recipe
    # No:
        # Ask what the user wants to change
        # Recommend next cocktail
    
    common.say(furhat, "What kind of occasion is the cocktail for?")

    # Wait for the user's response
    # For context, I made a custom function that calls their function.
    # The only thing that is changed, is that when the message is empty, succes should also be false.
    user_response = common.user_response(furhat)

    occasion = get_occasion(user_response.message)
    
    common.say(furhat, f"Fun to see your {occasion}! What kind of tastes do you prefer?")
    user_response = common.user_response(furhat)

    common.say(furhat, f"Nice! Let me look for the perfect cocktail for your {occasion}?", blocking=False)
    recommended_cocktail, ingredients, instructions = cosine_similarity.recommend_cocktail(f"{user_response.message} for {occasion}")
    
    common.say(furhat, f"For the {occasion} I recommend a {recommended_cocktail} cocktail. Would you like to make it?")
 
    # Wait for the user's response
    user_response = common.user_response(furhat)
    
    

    print(query(user_response.message, model='sentiment'))
    # Sentiment analysis on response user later on
    while query(user_response.message, model='sentiment') == "NEGATIVE":
        common.say(furhat, "Oh what can we change about the cocktail?")
        user_response = common.user_response(furhat)
        
        occasion = get_occasion(user_response.message)
        common.say(furhat, f"Good to see the {occasion}! Let me look for the best cocktail for you.", blocking=False)
                
        recommended_cocktail, ingredients, instructions = cosine_similarity.recommend_cocktail(user_response.message)
        

        common.say(furhat, "I recommend a " + recommended_cocktail + " cocktail. Would you like to make it?")

        user_response = common.user_response(furhat)
    
    # Update the user's model with the new cocktail
    user.last_drink = recommended_cocktail
    user.occasion = occasion
    database.update_user_data(user_id, user)

    common.say(furhat, "Great! Here are the ingredients and instructions.")
    common.say(furhat, ingredients)
    common.say(furhat, instructions)
