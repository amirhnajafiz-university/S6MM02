import matplotlib.pyplot as plt
from reader import read_image_file
from utils import rgb2gray


if __name__ == "__main__":
    path = "assets/image.png"  # input("[Enter the file path] > ")
    pix = read_image_file(path)

    pix = rgb2gray(pix)

    histogram = {}
    counter = 0

    for row in pix:
        for element in row:
            if element in histogram.keys():
                histogram[element]["intensity"] = histogram[element]["intensity"] + 1
            else:
                histogram[element] = {}
                histogram[element]["intensity"] = 1
                histogram[element]["sum"] = 0
                histogram[element]["normalized_sum"] = 0

        counter = counter + 1

    print(f'Histogram validation: {len(pix) == counter}')

    keys = histogram.keys()
    plt.stem(keys, [histogram[key]["intensity"] for key in histogram.keys()])
    plt.show()
