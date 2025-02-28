import speech_recognition as sr
import pyttsx3

# Recognizerを初期化する
r = sr.Recognizer()


# TTSのためのFUNCTION
def SpeakText(command: str) -> None:
    engine = pyttsx3.init()
    
    # Check and set the correct speech engine property on Linux
    engine.setProperty('voice', 'english')
    
    engine.say(command)
    engine.runAndWait()

PASSWORD: str = "hello"
POSSIBLE_ATTEMPTS: int = 5

def ask_password(password: str, possible_attempts: int) -> None:

    if not hasattr(ask_password, "wrong_count"):
        ask_password.wrong_count = 0  # 初期化
    SpeakText("Enter the password")
    try:
        # ユーザーのマイク入力を使う
        with sr.Microphone() as source2:

            # 周りの音に適応する
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # ユーザーの入力を聞く
            audio2 = r.listen(source2)

            # グーグルを使って文字起こしをする
            MyText: str = r.recognize_google(audio2)
            MyText = MyText.lower()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
        MyText = "failed"

    # 指定した回数だけユーザーにチャンスを与える
    if MyText == password:
        SpeakText("Correct")
    else:
        ask_password.wrong_count += 1
        SpeakText(f"Wrong. {possible_attempts - ask_password.wrong_count} attempts left")
        if possible_attempts - ask_password.wrong_count != 0:
            ask_password(PASSWORD, POSSIBLE_ATTEMPTS)
        else:
            SpeakText("Too many failed attempts")

ask_password(PASSWORD, POSSIBLE_ATTEMPTS)
