from time import time
import os
from PIL import Image, ImageFilter
import shutil
import multiprocessing


def main():
    URLs = collecting_URLs(os.getcwd())
    end_of_program = False

    if not os.path.isdir("{}/resized_img".format(os.getcwd())):
        os.mkdir("{}/resized_img".format(os.getcwd()))
    else:
        shutil.rmtree("{}/resized_img".format(os.getcwd()))
        end_of_program = True

    if not os.path.isdir("{}/resaved_img".format(os.getcwd())):
        os.mkdir("{}/resaved_img".format(os.getcwd()))
    else:
        shutil.rmtree("{}/resaved_img".format(os.getcwd()))
        end_of_program = True

    if not os.path.isdir("{}/refiltered_img".format(os.getcwd())):
        os.mkdir("{}/refiltered_img".format(os.getcwd()))
    else:
        shutil.rmtree("{}/refiltered_img".format(os.getcwd()))
        end_of_program = True

    if not os.path.isdir("{}/rerotated_img".format(os.getcwd())):
        os.mkdir("{}/rerotated_img".format(os.getcwd()))
    else:
        shutil.rmtree("{}/rerotated_img".format(os.getcwd()))
        end_of_program = True

    if not end_of_program:
        with multiprocessing.Pool() as executor:
            list_of_resized = [(url, 450, "{}/resized_img".format(os.getcwd()), i) for i, url in enumerate(URLs)]
            list_of_resaved = [(url, "{}/resaved_img".format(os.getcwd()), i) for i, url in enumerate(URLs)]
            list_of_refiltered = [(url, "{}/refiltered_img".format(os.getcwd()), ImageFilter.GaussianBlur(10), i) for
                                  i, url in
                                  enumerate(URLs)]
            list_of_rerotated = [(url, "{}/rerotated_img".format(os.getcwd()), 90, i) for i, url in enumerate(URLs)]

            executor.starmap(resizing_img, list_of_resized)
            executor.starmap(resaving_img, list_of_resaved)
            executor.starmap(refiltering_img, list_of_refiltered)
            executor.starmap(rerotating_img, list_of_rerotated)


def collecting_URLs(path):
    list_of_URLs = []
    for f in os.listdir(path):
        if f.endswith(".png"):
            list_of_URLs.append(f)

    return list_of_URLs


def resizing_img(image, size, path, name):
    i = Image.open(image)
    i.thumbnail([size, size])
    i.save("{}/image{}_{}.png".format(path, name, size))


def resaving_img(image, path, name):
    Image.open(image).save("{}/image{}.png".format(path, name))


def refiltering_img(image, path, filter, name):
    Image.open(image).filter(filter).save("{}/image{}_blured.png".format(path, name))


def rerotating_img(image, path, angle, name):
    Image.open(image).rotate(angle).save("{}/image{}_rotate.png".format(path, name))


if __name__ == "__main__":
    x1 = time()
    main()
    x2 = time()
    print("Elapsed time:{} sec(s)".format(round(x2 - x1, 3)))
