import nltk
import re
import time
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
from src.flow import buildModel, repeatSession


def extract_names(text: str):
    """
    Extracts named entities (names) from the given text.
    
    Args:
        text (str): The input text from which names are to be extracted.
        
    Returns:
        list: A list of extracted names.
    """
    names = []
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                names.append(''.join(c[0] for c in chunk))
    return names


def extract_numbers(text: str):
    """
    Extracts all the numbers from a given string.
    
    Args:
        s (str): The input string from which numbers are to be extracted.
        
    Returns:
        list: A list of all the numbers found in the input string.
    """
    return [int(num) for num in re.findall(r'\d+', text)]


def run(furhat: FurhatRemoteAPI):
    users = furhat.get_users()
    while not users:
        users = furhat.get_users()
        print("Looking for users. You can add a user in the Webinterface.")
        print("Password == admin, Go to Settings --> Microphone.")
        print("And then double click somewhere to spawn a user.")
        print()
        time.sleep(5)
        
    # Attend the user closest to the robot
    furhat.attend(user="CLOSEST")
    
    # Greetings from furhat
    common.say(furhat, "Hi there! I'm your conversational agent for recommending cocktails!")
    common.say(furhat, "Can you please let me know your name?")
    
    response = common.listen(furhat)
    
    if len(response.message.split()) > 1 or response.success == False:
        while 1:
            # Extract the name from the response
            names = extract_names(response.message)
            if len(names) == 1:
                name = names[0].title()
                break
            
            common.ask_to_repeat_name(furhat)
            response = common.listen(furhat)
            
            if len(response.message) == 1:
                name = response.message.title()
                break
    else:
        name = response.message.title()
        
    # Find user
    user_data = database.get_user_by_name(name)
    if user_data:
        user_data['visit'] += 1
        database.update_user_data(user_data)
        # If the user found in the database has visited before, go to repeatSession
        repeatSession.run(furhat, user_data)
        return
        
    # Extract the name from the response
    common.say(furhat, f"Nice to meet you {name}. Could I please know your age?")
    response_age = common.listen(furhat)
    ages = extract_numbers(response_age.message)
    while len(ages) != 1:
        common.ask_to_repeat(furhat)
        response_age = common.listen(furhat)
        ages = extract_numbers(response_age.message)
    age = ages[0]
    
    if age < 18:
        common.say(furhat, "I'm sorry, but you are too young to be drinking alcohol.")
        common.say(furhat, "Therefore I cannot recommend you any cocktails. I hope you understand.")
        return
    
    # Create user
    user_data = {
        'name': name,
        'age': age,
        'visit': 1,
        'last_drink': None,
        'preferred_sweet': None,
        'preferred_sour': None
    }
    database.insert_user_data(user_data)

    # Go to buildModel
    buildModel.run(furhat, user_data)
        
        
    
    
    # Start Conversation
    # Ask for name
    # If name is not known in database:
        # Ask for age
        # Go to buildModel.py
    # Else:
        # Go to repeatSession.py
    pass
