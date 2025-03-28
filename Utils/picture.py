import cv2
import os


def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1)-> str:
    cap = cv2.VideoCapture(device_num)
    
    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    ret, frame = cap.read()

    try:
        cv2.imwrite('{}.{}'.format(base_path, ext), frame)
        return '{}.{}'.format(base_path, ext)
    except Exception as e:
        print("failed to write image Error:{}".format(e))
        return "fail"
