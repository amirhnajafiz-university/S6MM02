from PIL import Image


def read_image_file(path):
    return Image.open(path, 'r')
