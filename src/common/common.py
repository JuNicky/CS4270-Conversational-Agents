import random
from furhat_remote_api import FurhatRemoteAPI
from swagger_client.models.status import Status


def listen(furhat: FurhatRemoteAPI):
    result = furhat.listen()
    if isinstance(result, Status):
        if result.message == '':
            result.success = False
        print(result)
        return result
    else:
        raise TypeError("Expected a Status object")
    
def user_response(furhat: FurhatRemoteAPI):
    user_response = listen(furhat)
    while not user_response.success:
        ask_to_repeat(furhat)

        user_response = listen(furhat)

    return user_response


def say(furhat: FurhatRemoteAPI, text: str, blocking: bool=True):
    furhat.say(text=text, blocking=blocking)


def ask_to_repeat(furhat: FurhatRemoteAPI):
    phrases = [
        "I'm sorry, I didn't catch that. Could you please say it again?",
        "Could you repeat that, please? I didn't quite hear you.",
        "Pardon me, I missed what you just said. Could you repeat?",
        "I'm sorry, could you say that one more time?",
        "I didn't hear that clearly, can you repeat it?"
    ]

    selected_phrase = random.choice(phrases)
    say(furhat, selected_phrase)
