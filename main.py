from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from reader import read_image_file
from utils import rgb2gray, create_histogram


if __name__ == "__main__":
    path = input("[Enter the file path] > ")
    pix, w, h = read_image_file(path)

    print(f'Image read: {w}x{h}')

    pix = rgb2gray(pix)

    histogram = create_histogram(pix, w, h, 0)
    keys = sorted(histogram.keys())

    newPix = []
    for row in range(h):  # apply the transformation
        temp = []
        for col in range(w):
            key = pix[row][col]
            element = histogram.get(key)
            temp.append(element["normalized_sum"])
        newPix.append(temp)

    img = Image.fromarray(np.asarray(newPix))
    img.show()

    newPix_histogram = create_histogram(newPix, w, h, 1)
    newPix_keys = sorted(newPix_histogram.keys())

    f, plt_array = plt.subplots(2, 2)
    plt_array[0][0].stem(keys, [histogram[key]["intensity"] for key in keys])
    plt_array[0][0].set_title("Intensity of colors of input image")
    plt_array[0][0].set_xlabel("Colors")
    plt_array[0][0].set_ylabel("Intensity")

    plt_array[0][1].stem(keys, [histogram[key]["sum"] for key in keys])
    plt_array[0][1].set_title("Cumulative sum of colors of input image")
    plt_array[0][1].set_xlabel("Colors")
    plt_array[0][1].set_ylabel("Cumulative sum")

    plt_array[1][0].stem(newPix_keys, [newPix_histogram[key]["intensity"] for key in newPix_keys])
    plt_array[1][0].set_title("Intensity of colors of transformed image")
    plt_array[1][0].set_xlabel("Colors")
    plt_array[1][0].set_ylabel("Intensity")

    plt_array[1][1].stem(newPix_keys, [newPix_histogram[key]["sum"] for key in newPix_keys])
    plt_array[1][1].set_title("Cumulative sum of colors of transformed image")
    plt_array[1][1].set_xlabel("Colors")
    plt_array[1][1].set_ylabel("Cumulative sum")

    plt.subplot_tool()
    plt.show()
