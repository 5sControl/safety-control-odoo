import face_recognition
from PIL import Image, ImageDraw

from .base_64_handlers import base64_encode, base64_decode

from ..static.img.get_path import get_file_name


def face_rec(image: str):

    # Decode the image
    path_to_image = base64_decode(image)

    # Get the coordinates of the points on the face
    face_img = face_recognition.load_image_file(path_to_image)
    face_location = face_recognition.face_locations(face_img)

    # Tracing the facial area
    pil_img = Image.fromarray(face_img)
    draw_img = ImageDraw.Draw(pil_img)

    for (top, right, bottom, left) in face_location:
        draw_img.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw_img

    pil_img.save(get_file_name() + 'img.jpg')

    # Encode the image
    encoded_image = base64_encode(get_file_name() + 'img.jpg')

    return encoded_image
