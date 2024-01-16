import requests

# Zephyr model
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
# Vind een question answering model en een text generation model dat lekker samenwerkt
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# input_string = "I am going to a party and I want something sweet"	

# gen_drink = query({
#         "inputs": """<|system|>
#     You are a chatbot who only recommends a cocktail based on user input without small talk and gives the ingredients. You only name cocktail and ingredients</s>
#     <|user|>""" + str(input_string) + """ </s>
#     <|assistant|>"""
#     })

# print(gen_drink)
# print(list(gen_drink[0].values())[0])
# print(output)