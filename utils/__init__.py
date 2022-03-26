import numpy as np


def rgb2gray(pic):  # get rgb input image and convert to gray scale
    return np.dot(pic[..., :3], [0.2989, 0.5870, 0.1140])
