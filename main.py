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
                histogram[element] = histogram[element] + 1
            else:
                histogram[element] = 1

        counter = counter + 1

    print(f'Histogram validation: {len(pix) == counter}')

    plt.stem(histogram.keys(), histogram.values())
    plt.show()
