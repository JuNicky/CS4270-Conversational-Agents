from furhat_remote_api import FurhatRemoteAPI
from src.common import database


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
    pass
