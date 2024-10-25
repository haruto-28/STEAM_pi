
import speech_recognition as sr
import pyttsx3 
from enum import Enum
 
# Initialize the recognizer 
r = sr.Recognizer() 
 
# Function to convert text to speech
def SpeakText(command: str) -> None:
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
        
PASSWORD: str = "hello"
POSSIBLE_ATTEMPTS: int = 5


def ask_password(password: str,possible_attempts: int) -> None:

    if not hasattr(ask_password, "wrong_count"):
        ask_password.wrong_count = 0  # it doesn't exist yet, so initialize it
    SpeakText("Enter the password")
    try:        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText:str = r.recognize_google(audio2)
            MyText = MyText.lower()
 
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
        MyText = "failed"

    if MyText == password:
        SpeakText("Correct")
    else:
        ask_password.wrong_count += 1
        print(MyText)
        SpeakText(f"wrong {possible_attempts - ask_password.wrong_count} attempts left") 
        if possible_attempts - ask_password.wrong_count != 0:
            ask_password(PASSWORD,POSSIBLE_ATTEMPTS)
        else:
            SpeakText("Too many failed attempts")

ask_password(PASSWORD,POSSIBLE_ATTEMPTS)
