import shutil
import os
import numpy as np  # pip install numpy
from multiprocessing import  Process


def prepare_images():
    list_of_images_path = os.listdir(f'{os.getcwd()}/images')
    for image_path in list_of_images_path:
        for x in range(500):
            shutil.copy(image_path,
                        f'{os.getcwd()}/existing_images/{x}{image_path}')


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def main():
    list_of_new_images = os.listdir(f'{os.getcwd()}/new_images')
    for new_image in list_of_new_images:
        ### create new process


if __name__ == '__main__':
    main()