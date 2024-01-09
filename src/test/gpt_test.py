# from transformers import pipeline, set_seed

# # Initialize a pipeline for text generation
# generator = pipeline('text-generation', model='gpt2')  # You can change 'gpt2' to other models

# # Example usage
# set_seed(42)
# text = "I feel happy and I'm looking for a cocktail with vodka and orange juice."
# generated_text = generator(text, max_length=50, num_return_sequences=1)

# print("here", generated_text[0]['generated_text'])

#Write code that uses a model that takes in a string which states the occasion and the taste preferences of the user and goes into a csv file and returns a list of cocktails that fit the occasion and taste preferences of the user. And after the user chooses a cocktail, the model should update the user's model and provide the recipe of the cocktail.

from transformers import pipeline, set_seed
import pandas as pd
import numpy as np
import random

# Initialize a pipeline for text generation
generator = pipeline('text-generation', model='gpt2')  # You can change 'gpt2' to other models

# Example usage
set_seed(42)

# Read the csv file
df = pd.read_csv('data/cocktails.csv')
df = df.dropna()
df = df.reset_index(drop=True)

# Get the list of ingredients
ingredients = df['Ingredients'].tolist()

# Get the list of occasions
occasions = df['Occasion'].tolist()