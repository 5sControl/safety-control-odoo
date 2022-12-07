import face_recognition
from PIL import Image, ImageDraw

from scripts.base_64_handlers import base64_encode, base64_decode


def face_rec(image: bytes):

    # Decode the image
    path_to_image = base64_decode(image)

    # Get the coordinates of the points on the face
    face_img = face_recognition.load_image_file(path_to_image)
    face_location = face_recognition.face_locations(face_img)

    # Tracing the facial area
    pil_img = Image.fromarray(face_img)
    draw_img = ImageDraw.Draw(pil_img)

    for(top, right, bottom, left) in face_location:
        draw_img.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw_img
    pil_img.save("custom/safety_control/static/img/imgf.jpg")

    # Encode the image
    encoded_image = base64_encode('custom/safety_control/static/img/imgf.jpg')

    return encoded_image