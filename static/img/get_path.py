import os


def get_file_name():
    path_to_image_dir = os.path.abspath(__file__)[:-11]
    return path_to_image_dir
