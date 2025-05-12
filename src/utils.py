def process_image(image_path):
    import cv2
    import numpy as np
    from face_recognition import load_image_file, face_encodings

    image = load_image_file(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_enc = face_encodings(image)

    if face_enc:
        return face_enc[0]
    return None

def save_image(image, path):
    from PIL import Image
    image.save(path)

def encode_face(face_encoding):
    import base64
    return base64.b64encode(face_encoding).decode('utf-8')

def decode_face(encoded_face):
    import base64
    return np.frombuffer(base64.b64decode(encoded_face), dtype=np.float64)