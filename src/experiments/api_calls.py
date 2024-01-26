import requests

API_dict = {
    "sentiment": "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english",
    "recommend": "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0",
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
    print("Occasion: " ,qa_occasion)
    return list(qa_occasion.values())[-1]


#write a main Function
if __name__ == "__main__":
    #cal the apicall with recommended cocktail
    gen_drink = query({
        "inputs": """<|system|>
    You are a chatbot who recommends a cocktail based on user input and gives the ingredients</s>
    <|user|>""" + "a sweet and sour taste for a party" + """ </s>
    <|assistant|>"""
    }, model='recommend')
    print(gen_drink)
    # print("=====================================")
    # print(gen_drink[0]['generated_text'])
