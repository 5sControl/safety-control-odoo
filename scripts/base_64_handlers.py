import pybase64

from PIL import Image
from io import BytesIO

from ..static.img.get_path import get_file_name


def base64_encode(data_image):
    with open(data_image, "rb") as image_file:
        return pybase64.b64encode(image_file.read())


def base64_decode(data_image):
    image = Image.open(BytesIO(pybase64.b64decode(data_image)))
    image.save(get_file_name() + 'image.jpg')
    return get_file_name() + 'image.jpg'

