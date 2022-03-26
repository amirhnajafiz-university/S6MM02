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

    keys = sorted(histogram.keys())

    for index in range(len(keys)):
        current = keys[index]
        if index == 0:
            histogram[current]["sum"] = histogram[current]["intensity"]
        else:
            histogram[current]["sum"] = histogram[current]["intensity"] + histogram[keys[index-1]]["sum"]

    f, plt_array = plt.subplots(2)
    plt_array[0].stem(keys, [histogram[key]["intensity"] for key in keys])
    plt_array[1].stem(keys, [histogram[key]["sum"] for key in keys])
    plt.show()
