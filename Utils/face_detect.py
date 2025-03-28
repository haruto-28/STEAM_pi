import cv2
import time 

# カスケード分類器を手動で読み込む
face_cascade = cv2.CascadeClassifier('opencv-data/haarcascade_frontalface_default.xml')

# Haarカスケード分類器が正しく読み込まれたかチェック
if face_cascade.empty():
    print("Haarカスケード分類器の読み込みに失敗しました。")
    exit()
    
def detect_face(path:str)-> bool:
    try:
        image = cv2.imread(path)  
    except Exception as e:
        return False

    # 画像をグレースケールに変換（顔検出のため）
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

    if len(faces) == 0:
        return False
    else:
        return True