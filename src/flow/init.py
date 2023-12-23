import time
from furhat_remote_api import FurhatRemoteAPI
from src.common import common


def run(furhat: FurhatRemoteAPI):
    # Get the users detected by the robot 
    users = furhat.get_users()
    while not users:
        users = furhat.get_users()
        print("Looking for users. You can add a user in the Webinterface.")
        print("Password == admin, Go to Settings --> Microphone.")
        print("And then double click somewhere to spawn a user.")
        time.sleep(5)

    # Attend the user closest to the robot
    furhat.attend(user="CLOSEST")

    # Greetings from furhat
    furhat.say(text="Hi there, I'm Formula-man!",)
    furhat.say(text="Nice to meet you! I haven't seen you before. What's your name?")

    # I could not make the furhat.say asynchronous. We still need to fix that.
    # What would happen if you didn't inclunde the next line is that furhat would already listen
    # while the user was not done talking yet.
    time.sleep(7)

    # Wait for the user's response
    # For context, I made a custom function that calls their function.
    # The only thing that is changed, is that when the message is empty, succes should also be false.
    user_response = common.listen(furhat)
    while not user_response.success:
        common.ask_to_repeat(furhat)

        # Here aswell (see line 23-25)
        time.sleep(5)

        user_response = common.listen(furhat)

    furhat.say(text="This was the end of the demo.")
 