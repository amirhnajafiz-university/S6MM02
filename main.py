from reader import read_image_file


if __name__ == "__main__":
    path = input("[Enter the file path] > ")
    pix = read_image_file(path)
    print(pix)
