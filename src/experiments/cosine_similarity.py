import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LogisticRegression
# Load the dataset
data = pd.read_csv('src/experiments/cocktail_data.csv', encoding='ISO-8859-1')

# Preprocess the data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['ingredients_and_quantities'])

# Train a logistic regression model to predict occasion/mood
model = LogisticRegression()
model.fit(X, data['drink'])

# Function to recommend a cocktail based on input string
def recommend_cocktail(input_string):
    # Preprocess the input string
    input_vector = vectorizer.transform([input_string])

    # Predict the drink of the input string
    predicted_drink = model.predict(input_vector)[0]

    # Filter the dataset based on predicted drink
    filtered_data = data[data['drink'] == predicted_drink]

    # Reset the index of the filtered data
    filtered_data = filtered_data.reset_index()

    # Calculate cosine similarity between input and filtered dataset
    filtered_X = vectorizer.transform(filtered_data['ingredients_and_quantities'])
    similarity_scores = cosine_similarity(input_vector, filtered_X)
    print(similarity_scores)
    # Find the index of the most similar cocktail in the filtered dataset
    most_similar_index = similarity_scores.argmax()

    # Return the recommended cocktail
    recommended_cocktail = filtered_data.loc[most_similar_index, 'drink']
    # assign ingredients_and_quantities to a variable
    ingredients_and_quantities = filtered_data.loc[most_similar_index, 'ingredients_and_quantities']
    # assign instructions to a variable
    instructions = filtered_data.loc[most_similar_index, 'instructions']
    return recommended_cocktail, ingredients_and_quantities, instructions


# Example usage
input_string = "fruity"
recommended_cocktail = recommend_cocktail(input_string)
print("Recommended cocktail:", recommended_cocktail)
