import cv2
import time 
# ウェブカメラを開く
cap = cv2.VideoCapture(0)  # 0はパソコンにつないだ最初のカメラを指す

# カメラが開けたかチェック
if not cap.isOpened():
    print("カメラを開けませんでした。")
    exit()

while True:
    ret, frame = cap.read()

    # キャプチャした画像が正しいかチェック
    if not ret:
        print("画像をキャプチャできませんでした。")
        break

    # ここで画像に対して何らかの処理を行い、その結果をファイルに保存することができます
    cv2.imwrite('image_one.jpg', frame) 
    # 例: cv2.imwrite('captured_image.jpg', frame)  # 画像をファイルとして保存
    break

# カメラを閉じます
cap.release()
# cv2.destroyAllWindows() # これもウィンドウ関連なので削除します
time.sleep(1)

# カスケード分類器を手動で読み込む
face_cascade = cv2.CascadeClassifier('/home/kali/STEAM_pi/haarcascade_frontalface_default.xml')

# 画像を読み込む
image = cv2.imread('image_one.jpg')  # 'image_one.jpg' は顔検出したい画像ファイル名に変更

# 画像をグレースケールに変換（顔検出のため）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔を検出する
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# 検出された顔に枠を描く
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 赤色の枠

# 結果を保存する
cv2.imwrite('output_image.jpg', image)  # 'output_image.jpg' に結果を保存