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


def ask_to_repeat_name(furhat: FurhatRemoteAPI):
    phrases = [
        "Apologies, I missed your name. Could you say it again, please?",
        "I'm sorry, your name slipped past me. Would you mind repeating it?",
        "Pardon me, I didn't quite get your name. Can you repeat it, please?",
        "Sorry, I didn't hear your name clearly. Could you tell me again?",
        "Excuse me, I failed to catch your name. Would you please repeat it?"
    ]

    selected_phrase = random.choice(phrases)
    say(furhat, selected_phrase)
