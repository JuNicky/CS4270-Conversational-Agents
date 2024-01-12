import requests

# Zephyr model
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
# Google model
# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xl"

# Vind een question answering model en een text generation model dat lekker samenwerkt
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

output = query({
	"inputs": "I'm planning a girls night out and I want to make a signature cocktail for the group. Can you recommend a cocktail that is easy to make and has a sweet taste?"
})

# print(list(output[0].values())[0])
print(output)