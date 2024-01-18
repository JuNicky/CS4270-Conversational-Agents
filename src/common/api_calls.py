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


def get_occasion(input_string):
    qa_occasion = query({
        "inputs": {
            "question": "What is the occasion mentioned?",
            # "context": list(gen_drink[0].values())[0]
            "context": str(input_string)
        },
    }, model='qa')

    return list(qa_occasion.values())[-1]


input_string = "I would like a sweet cocktail"	

gen_drink = query({
        "inputs": """<|system|>
    Is there an occasion mentioned by the user?</s>
    <|user|>""" + str(input_string) + """ </s>
    <|assistant|>"""
    }, model='recommend')

print(gen_drink[0]['generated_text'])

print(query(list(gen_drink[0].values())[0], model='sentiment'))