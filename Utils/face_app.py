import face_recognition


class face_detector:

    def __init__(self,path:str)-> None:
        # Load the reference image and encode the face
        self.reference_image = face_recognition.load_image_file(path)  
        self.reference_encoding = face_recognition.face_encodings(self.reference_image)[0]

    def detect_face(self,rgb_frame) -> bool:
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces([self.reference_encoding], face_encoding)

            if matches[0]:
                return True


