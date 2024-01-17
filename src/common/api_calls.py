import requests

API_dict = {
    "sentiment": "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english",
    "recommend": "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta",
    "qa": "https://api-inference.huggingface.co/models/timpal0l/mdeberta-v3-base-squad2"
}

headers = {"Authorization": "Bearer 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"}

def query(payload, model):
    response = requests.post(API_dict[model], headers=headers, json=payload)
    if model == 'sentiment':
        return list(response.json()[0][0].values())[0]
    return response.json()