import numpy as np


def rgb2gray(pic):  # get rgb input image and convert to gray scale
    return np.dot(pic[..., :3], [0.2989, 0.5870, 0.1140])


def transform_cell(c_sum, width, height, color_levels):  # the transform function
    return round(((color_levels - 1) * c_sum) / (width * height))


def create_histogram(pix, w, h, histogram_id):
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

    print(f'[{histogram_id}] Histogram validation: {len(pix) == counter}')

    keys = sorted(histogram.keys())

    for index in range(len(keys)):
        current = keys[index]
        if index == 0:
            histogram[current]["sum"] = histogram[current]["intensity"]
        else:
            histogram[current]["sum"] = histogram[current]["intensity"] + histogram[keys[index - 1]]["sum"]

    total = len(keys)
    for key in keys:  # transform each of the colors
        histogram[key]["normalized_sum"] = transform_cell(histogram[key]["sum"], w, h, total)

    return histogram
