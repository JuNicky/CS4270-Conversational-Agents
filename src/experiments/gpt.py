import requests

# Zephyr model
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
# Vind een question answering model en een text generation model dat lekker samenwerkt
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

input_string = "I would like a sweet cocktail"	

gen_drink = query({
        "inputs": """<|system|>
    Is there an occasion mentioned by the user?</s>
    <|user|>""" + str(input_string) + """ </s>
    <|assistant|>"""
    })

print(gen_drink)
print(list(gen_drink[0].values())[0])