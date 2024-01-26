from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained model tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_embedding(text):
    # Encode text and return the embedding
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(1)

# Define embeddings for each flavor
flavor_embeddings = {flavor: get_embedding(flavor) for flavor in ["sweet", "sour", "spicy", "bitter", "fruity", "savory", "hot", "frozen", "refreshing"]}

def classify_flavor(food_item):
    # Get embedding for the food item
    food_embedding = get_embedding(food_item)

    # Compare with flavor embeddings to find the closest match
    closest_flavor = None
    min_distance = float('inf')
    for flavor, embedding in flavor_embeddings.items():
        distance = torch.norm(food_embedding - embedding)
        if distance < min_distance:
            min_distance = distance
            closest_flavor = flavor

    return closest_flavor

# Example usage
food_item = "lemon"
flavor = classify_flavor(food_item)
print(f"The flavor of '{food_item}' is {flavor}.")
