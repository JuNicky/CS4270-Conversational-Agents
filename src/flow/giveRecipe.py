import random
from furhat_remote_api import FurhatRemoteAPI
from src.common import common


def run(furhat: FurhatRemoteAPI, name, ingredients, instructions):
    phrases = [
        f"Great! Here are the ingredients and instructions for {name}.",
        f"Awesome! Let me provide you with the ingredients and the preparation steps for {name}.",
        f"Excellent! I'll now share the ingredients and how-to guide for making {name}.",
        f"Wonderful! Here's what you'll need and the instructions to create {name}.",
        f"Fantastic! I have the list of ingredients and the method for preparing {name} ready for you.",
    ]
    selected_phrase = random.choice(phrases)
    common.say(furhat, selected_phrase)
    common.say(furhat, ingredients)
    common.say(furhat, instructions)