from PIL import Image
import numpy as np


def read_image_file(path):
    # Opening the image file
    pic = Image.open(path, 'r')

    return np.asarray(pic)  # returning the image as array
