import requests

# Zephyr model
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
# Vind een question answering model en een text generation model dat lekker samenwerkt
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

	

# output = query({
# 	"inputs": """<|system|>
# You are a chatbot who recommends cocktails based on user input</s>
# <|user|>
# I want something for a wedding</s>
# <|assistant|>"""
# })

# print(type(list(output[0].values())[0]))
# print(output)