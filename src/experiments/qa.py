import requests

API_URL = "https://api-inference.huggingface.co/models/timpal0l/mdeberta-v3-base-squad2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"question": "Did the user mention an occasion?",
		"context": "I want to eat a hamburger at my party"
	},
})

print(output)