import os
import numpy as np
import cv2


INT_SIZE = 4
UTF_8_CHAR_SIZE = 4

class setting_file:
    def __init__(self,img: str = None,pin1:list = None,pin_to_change: list = None,mail_address:str = None,file: str = None):
        self.img = img
        self.pin1 = pin1
        self.pin2 = pin_to_change
        self.mail_adress = mail_address
        self.file = file

    def read_file(self):
        file_size = os.path.getsize(self.file)
        with open(self.file, 'rb') as f:
        
            # Read PIN_1 and PIN_2 values using list comprehensions
            PIN_1_SIZE = INT_SIZE * 5
            self.pin1 = [int.from_bytes(f.read(INT_SIZE), "big") for i in range(1, 6)]

            PIN_2_SIZE = INT_SIZE * 5
            self.pin2 = [int.from_bytes(f.read(INT_SIZE), "big") for i in range(1, 6)]

            # Read mail string data
            MAIL_STRING_SIZE_SIZE = INT_SIZE
            MAIL_STRING_SIZE = int.from_bytes(f.read(INT_SIZE), "big")
            self.mail_adress = f.read(MAIL_STRING_SIZE).decode('utf-8')

            #read the rest of the file
            image = f.read(file_size - (PIN_1_SIZE + PIN_2_SIZE + MAIL_STRING_SIZE_SIZE + MAIL_STRING_SIZE))
            # Convert the byte data into a NumPy array (OpenCV works with NumPy arrays)
            image_array = np.frombuffer(image, dtype=np.uint8)

            # Decode the image from the byte array using OpenCV
            self.img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    def write_file(self):
        with open("setting.secset", "wb") as output_file:
            for i in self.pin1:
                output_file.write(i.to_bytes(INT_SIZE, byteorder='big'))
            for i in self.pin2:
                output_file.write(i.to_bytes(INT_SIZE, byteorder='big'))

            output_file.write(len(self.mail_adress.encode("utf-8")).to_bytes(INT_SIZE, byteorder='big'))
            output_file.write(self.mail_adress.encode("utf-8")) #utf-8 endcoding

            try:
                with open(self.img, 'rb') as f:
                    img_data = f.read()
                output_file.write(img_data)

            except Exception as e:

                print("failed to open image error:{}".format(e))
                return 0
        
    def __str__(self):
        return"pin1:{}\npin2:{}\nemail:{}".format(self.pin1,self.pin2,self.mail_adress)


