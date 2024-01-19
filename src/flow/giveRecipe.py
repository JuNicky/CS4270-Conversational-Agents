import random
from furhat_remote_api import FurhatRemoteAPI
from src.common import common, database
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
        label = EMOTIONS[preds.argmax()]
        print(label)
        return label
    else:
        print("Face not found")
        return "neutral"


def run(furhat: FurhatRemoteAPI, cocktail, user):
    print("Recommended cocktail: ", cocktail)
    user.last_drink = cocktail.drink
    user.sour = cocktail.sour
    user.sweet = cocktail.sweet
    user.cream = cocktail.cream
    user.bitter = cocktail.bitter
    user.water = cocktail.water
    user.herbal = cocktail.herbal
    user.egg = cocktail.egg
    user.salty = cocktail.salty
    user.spicy = cocktail.spicy
    database.update_user_data(user.id, user)
    emotion = emotion_analysis()
    phrases = [
        f"Here are the ingredients and instructions for {cocktail.drink}.",
        f"Let me provide you with the ingredients and the preparation steps for {cocktail.drink}.",
        f"I'll now share the ingredients and how-to guide for making {cocktail.drink}.",
        f"Here's what you'll need and the instructions to create {cocktail.drink}.",
        f"I have the list of ingredients and the method for preparing {cocktail.drink} ready for you.",
    ]
    selected_phrase = random.choice(phrases)
    emotion_responses = {
        "angry": "I see from your face that you feel a bit angry. Don't worry, this cocktail will pleasantly surprise you.",
        "disgust": "I see from your face that you feel a bit disgusted. Don't worry, this cocktail will pleasantly surprise you.",
        "scared": "I see from your face that you feel a bit scared. Don't worry, this cocktail will pleasantly surprise you.",
        "happy": "I see from your face that you feel a bit happy. I'm glad to see that!",
        "sad": "I see from your face that you feel a bit sad. Don't worry, this cocktail will pleasantly surprise you.",
        "surprised": "I see from your face that you feel a bit surprised. Don't worry, this cocktail will pleasantly surprise you.",
        "neutral": "I see from your face that you feel a bit neutral. Don't worry, this cocktail will pleasantly surprise you."
    }

    emotion_phrase = emotion_responses.get(emotion, "I cannot see from your face how you're feeling, but I hope you'll enjoy this cocktail!")
    
    common.say(furhat, emotion_phrase)
    common.say(furhat, selected_phrase)
    common.say(furhat, cocktail.ingredients_and_quantities)
    common.say(furhat, cocktail.instructions)