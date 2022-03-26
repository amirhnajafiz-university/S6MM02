from reader import read_image_file
from utils import rgb2gray


if __name__ == "__main__":
    path = input("[Enter the file path] > ")
    pix = read_image_file(path)

    pix = rgb2gray(pix)

    print(len(pix))
