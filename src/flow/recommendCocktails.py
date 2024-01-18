import time
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
from src.common.api_calls import query, get_occasion
from src.experiments import cosine_similarity, sentiment_analysis


from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np

detection_model_path = 'emotionRecognition/haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'emotionRecognition/models/_mini_XCEPTION.102-0.66.hdf5'

face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised", "neutral"]

cv2.namedWindow('your_face')
camera = cv2.VideoCapture(0)

def emotion_analysis():
    frame = camera.read()[1]
    #reading the frame
    frame = imutils.resize(frame,width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()

    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
        key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
                    # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
            # the ROI for classification via the CNN
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        
        
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]
        print(label)
    else: return "neutral"
    
    return label



# Recommends cocktails to the user based on their preferences
def run(furhat: FurhatRemoteAPI, user_id, user):
    # Calculate cocktail using cosine similarity
    # Ask if the user wants the cocktail
    # Yes:
        # Update the user's model
        # Provide the recipe
    # No:
        # Ask what the user wants to change
        # Recommend next cocktail
    
    common.say(furhat, "What kind of cocktail would you like?")

    # Wait for the user's response
    # For context, I made a custom function that calls their function.
    # The only thing that is changed, is that when the message is empty, succes should also be false.
    user_response = common.user_response(furhat)
    
    occasion = get_occasion(user_response.message)
    
    common.say(furhat, f"Fun to see your {occasion}! Let me look for the best cocktail for you.", blocking=False)
    recommended_cocktail, ingredients, instructions,  = cosine_similarity.recommend_cocktail(user_response.message)

    common.say(furhat, f"For the {occasion} I recommend a {recommended_cocktail} cocktail. Would you like to make it?")
    
    # Wait for the user's response
    user_response = common.user_response(furhat)
    
    

    print(query(user_response.message, model='sentiment'))
    # Sentiment analysis on response user later on
    while query(user_response.message, model='sentiment') == "NEGATIVE":
        common.say(furhat, "Oh what can we change about the cocktail?")
        user_response = common.user_response(furhat)
        
        occasion = get_occasion(user_response.message)
        common.say(furhat, f"Good to see the {occasion}! Let me look for the best cocktail for you.", blocking=False)
                
        recommended_cocktail, ingredients, instructions = cosine_similarity.recommend_cocktail(user_response.message)
        

        common.say(furhat, "I recommend a " + recommended_cocktail + " cocktail. Would you like to make it?")

        user_response = common.user_response(furhat)
    
    # Update the user's model with the new cocktail
    user.last_drink = recommended_cocktail
    user.occasion = occasion
    database.update_user_data(user_id, user)

    common.say(furhat, "Great! Here are the ingredients and instructions.")
    common.say(furhat, ingredients)
    common.say(furhat, instructions)
