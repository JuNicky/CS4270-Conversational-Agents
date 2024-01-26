import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
from src.common.api_calls import query
from src.common import database
# from api_calls import query

# import gpt, qa
# Load the dataset
data = pd.read_csv('src/experiments/updated_cocktail_data.csv', encoding='ISO-8859-1')

# Preprocess the data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['ingredients_and_quantities'])


def extract_ingredients(text):
    """
    Extracts and formats the ingredients from a given text.

    Parameters:
    text (str): The input text containing ingredients listed in a specific format.

    Returns:
    str: A string containing the extracted ingredients, separated by commas.
    """
    # Splitting the text into lines
    lines = text.split('\n')

    # Extracting the lines that contain ingredients
    ingredients = [line.strip('- ').split('(')[0].strip() for line in lines if '- ' in line]

    # Joining the ingredients with a comma
    formatted_ingredients = ', '.join(ingredients)
    return formatted_ingredients

# Function to recommend a cocktail based on input string
def recommend_cocktail(input_string, second_try=False):

    # stukje gptflow
    gen_drink = query({
        "inputs": """<|system|>
    You are a chatbot who recommends a cocktail based on user input and gives the ingredients</s>
    <|user|>""" + str(input_string) + """ </s>
    <|assistant|>"""
    }, model='recommend')
    # print(gen_drink)
    # print("=====================================")
    # print(gen_drink[0]['generated_text'])

    # Question answering model
    qa_recommend = query({
        "inputs": {
            "question": "What is the cocktail recommended?",
            "context": str(input_string)
        },
    }, model='qa')
    print(qa_recommend)

    gen_ingredients = extract_ingredients(gen_drink[0]['generated_text'])

    # Preprocess the input string
    input_vector = vectorizer.transform([gen_ingredients])

    # Calculate cosine similarity between input and filtered dataset
    filtered_X = vectorizer.transform(data['ingredients_and_quantities'])
    similarity_scores = cosine_similarity(input_vector, filtered_X)
    print(similarity_scores)
    # Find the index of the most similar cocktail in the filtered dataset
    if second_try:
        most_similar_index = similarity_scores[0][1:].argmax()
        
    else:
        most_similar_index = similarity_scores.argmax()

    # Return the recommended cocktail
    recommended_cocktail = data.loc[most_similar_index, 'drink']

    print("Recommended cocktail:", recommended_cocktail)
    return database.get_drink_by_cocktail(recommended_cocktail)


if __name__ == "__main__":
    # Example usage
    input_string = "I would like a strong and sweet drink fo my girls party"
    recommended_cocktail = recommend_cocktail(input_string)
    print("Recommended cocktail:", recommended_cocktail)
