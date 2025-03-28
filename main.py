from datetime import datetime
from Utils.notify import send_mail
import Utils.picture
import Utils.face_app
import Utils.face_detect
import Utils.settings
import cv2
import numpy as np


# Start video capture
video_capture = cv2.VideoCapture(0)

def get_settings()-> Utils.settings.setting_file:
    try:
        setting_file = Utils.settings.setting_file(file="setting.secset")
        ask = input("設定を変更しますか？(y/n)")
        print(ask)
        if  ask == "y":
            email = input("email:")
            pin = list(input("五文字のパスワードを入力してください："))
            print("写真を撮ります")
            while True:
                if input("準備ができましたか?(y/n)") == "y":
                    path = Utils.picture.save_frame_camera_key(0,"data/","test")
                if Utils.face_detect.detect_face("data/test.jpg") == False:
                    print("顔が検出できなかったためもう一回とります")
                else:
                    break
            setting_file = Utils.settings.setting_file(img=path,pin1= [int(i) for i in pin],pin_to_change = [int(i) for i in pin],mail_address=email)
            setting_file.write_file()
            return setting_file
        else:
            setting_file.read_file()
            return setting_file
    except Exception as e:
        print(e)
        email = input("email:")
        pin = list(input("五文字のパスワードを入力してください："))
        print("写真を撮ります")
        while True:
            if input("準備ができましたか?(y/n)") == "y":
                path = Utils.picture.save_frame_camera_key(0,"data/","test")
            if Utils.face_detect.detect_face("data/test.jpg") == False:
                print("顔が検出できなかったためもう一回とります")
            else:
                break
        setting_file = Utils.settings.setting_file(img=path,pin1= [int(i) for i in pin],pin_to_change = [int(i) for i in pin],mail_address=email)
        setting_file.write_file()
        return setting_file

setting_file = get_settings()
fd = Utils.face_app.face_detector("data/test.jpg")

with open("pass.txt", "r") as file:
    password = file.read()

if __name__ == "__main__":

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("???")
            break
        ask = input("開錠しますか?(y/n)") 
        if ask == "y":
            if fd.detect_face(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)):
                Utils.picture.save_frame_camera_key(0,"security/ok","alert_{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            else:
                pic = Utils.picture.save_frame_camera_key(0,"security/bad","alert_{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                send_mail("s3cur1t7St3am@gmail.com",password,"s3cur1t7St3am@gmail.com",setting_file.mail_adress,pic,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Release resources
video_capture.release()
