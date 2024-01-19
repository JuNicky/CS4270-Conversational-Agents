import random
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
from src.experiments import cosine_similarity, sentiment_analysis
from src.flow import buildModel, recommendCocktails, giveRecipe

# We only reach this function once it's at least the 2nd time encountering the user
def run(furhat: FurhatRemoteAPI, user_data):
    print("We are currently running repeatSession.py") 
    # If the user wants to change their recipe
        # Go to buildModel
    # Else
        # Go to recommend cocktails
        
    print("User data: ", user_data)
    last_drink = user_data.last_drink
    print("last drink: ", last_drink)
    common.say(furhat, f"Welcome back {user_data.name}! I'm glad to see you again.")
    common.say(furhat, f"I remember that I gave you {last_drink} last time. How did you like your drink?")
    
    # Wait for the user's response
    user_response = common.user_response(furhat)

    # Sentiment analysis on response
    if sentiment_analysis.query(user_response.message) == "NEGATIVE":
        common.say(furhat, "I'm sorry to hear you didn't like your drink. Is there something that I can change on the taste?")
        user_response = common.user_response(furhat)
        
        sentiment = sentiment_analysis.query(user_response.message)
        flavors = ['sour','sweet','cream','bitter','water','herbal','egg','salty','spicy']
        for i in flavors:
            if i in user_response.message:
                print(sentiment)
                database.change_flavour_profile(user_data.id, i, sentiment == "POSITIVE")
                updated_user = database.get_user_by_id(user_data.id)
                drinks = database.get_drinks_based_on_user(updated_user)
                if len(drinks) == 0:
                    break
                common.say(furhat, f"Alright, let me look for new recommendations.")
                if len(drinks) == 1:
                    drink = drinks[0]
                    common.say(furhat, f"I found one recommendation for you, the {drink}. Would you like to make it?")
                    user_response = common.user_response(furhat)
                    sentiment = sentiment_analysis.query(user_response.message)
                    if sentiment == "POSITIVE":
                        giveRecipe.run(furhat, drink, user_data)
                    break
                if len(drinks) > 1:
                    drink = drinks.pop(0)
                    common.say(furhat, f"I found a few recommendations for you. I recommend you the {drink.drink}. Would you like to make it?")
                    user_response = common.user_response(furhat)
                    sentiment = sentiment_analysis.query(user_response.message)
                    if sentiment == "POSITIVE":
                        giveRecipe.run(furhat, drink, user_data)
                        return
                    while sentiment == "NEGATIVE" and len(drinks) > 0:
                        drink = drinks.pop(0)
                        phrases = [
                            f"Alright, how about I suggest the {drink.drink}? Are you interested in making it?",
                            f"Let's go with the {drink.drink}. Does making this one sound good to you?",
                            f"Okay, I propose the {drink.drink} for you. Would you like to try preparing it?"
                        ]
                        selected_phrase = random.choice(phrases)
                        common.say(furhat, selected_phrase)
                        user_response = common.user_response(furhat)
                        sentiment = sentiment_analysis.query(user_response.message)
                        if sentiment == "POSITIVE":
                            giveRecipe.run(furhat, drink, user_data)
                            return
                    break
                
        # Cannot find flavour or no drinks found
        common.say(furhat, "I couldn't find you a cocktail based on your preferences.")
        cocktail = database.get_random_cocktail()
        common.say(furhat, f"But I found a cocktail that you might like. It is called {cocktail.drink}. Would you like to make it?")
        user_response = common.user_response(furhat)
        sentiment = sentiment_analysis.query(user_response.message)
        while sentiment == "NEGATIVE":
            cocktail = database.get_random_cocktail()
            phrases = [
                f"I'm sorry the previous cocktail wasn't to your taste. I've searched for other options and suggest you try {cocktail.drink}. Does that sound good to you?",
                f"Apologies for the last cocktail not meeting your preferences. However, I've found a different one, {cocktail.drink}, which might be more to your liking. Your thoughts?",
                f"Regretful to learn the last cocktail didn't appeal to you. I've explored other choices and would like to propose {cocktail.drink}. Would you like to give it a try?",
                f"It's unfortunate that the previous cocktail wasn't a hit. I've looked into other selections and have {cocktail.drink} as a recommendation. How does that strike you?",
                f"Sorry the last cocktail wasn't a favorite. I've done some searching and think {cocktail.drink} could be a great alternative. Interested in trying it?"
            ]
            selected_phrase = random.choice(phrases)
            common.say(furhat, selected_phrase)
            user_response = common.user_response(furhat)
            sentiment = sentiment_analysis.query(user_response.message)
                

    else:
        common.say(furhat, "I'm glad to hear you liked your drink. Would you like to make it again?")
        user_response = common.user_response(furhat)
        sentiment = sentiment_analysis.query(user_response.message)
        if sentiment == "POSITIVE":
            cocktail = database.get_drink_by_cocktail(last_drink)
        else:
            common.say(furhat, "Alright, let's find you a new cocktail.")
            recommendCocktails.run(furhat, user_data.id, user_data)

    giveRecipe.run(furhat, cocktail, user_data)
    return
