import concurrent.futures
import os
from PIL import Image
from time import time
from concurrent import futures
from multiprocessing import Pool


def main():
    path = "images/"
    URLs = list_of_URLs(os.getcwd())
    list_of_args = []
    if not os.path.isdir(path):
        os.mkdir(path)

    for i, url in enumerate(URLs):
        list_of_args.append([url, path, "image{}.png".format(i + 1)])

    with Pool() as executor:
        executor.starmap(resave_rename_img, list_of_args)


def list_of_URLs(path):
    list_of_img = []
    for f in os.listdir(path):
        if f.endswith(".png"):
            list_of_img.append(Image.open(f))

    return list_of_img


def resave_rename_img(image, path, name):
    img_name = os.path.join(path, name)
    image.save(img_name)


if __name__ == "__main__":
    x1 = time()
    main()
    x2 = time()
    print("Time:{} sec(s)".format(round(x2 - x1, 2)))
