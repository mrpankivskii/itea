import shutil
import os
import numpy as np  # pip install numpy

import cv2

from time import time
from multiprocessing import Process


def prepare_images():
    list_of_images_path = os.listdir(f'{os.getcwd()}/images')
    for image_path in list_of_images_path:
        for x in range(500):
            shutil.copy(f'{os.getcwd()}/images/{image_path}',
                        f'{os.getcwd()}/existing_images/{x}{image_path}')


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def process_images(images_list):
    existing_images_path = f'{os.getcwd()}/existing_images'
    existing_images_list = os.listdir(existing_images_path)
    existing_images_list = [cv2.imread(f'{existing_images_path}/{x}')
                            for x in existing_images_list]
    for new_image in images_list:
        image0 = cv2.imread(f'{os.getcwd()}/new_images/{new_image}')
        for image in existing_images_list:
            err = mse(image0, image)
            if err < 6000:
                print(f'Similar to already exist {new_image}')
                break
        # os.rename(f'{os.getcwd()}/new_images/{new_image}',
        #           f'{os.getcwd()}/done_images/{new_image}')


def timeit(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(time() -  start)
        return result
    return inner


@timeit
def main():
    # prepare_images()

    list_of_new_images = os.listdir(f'{os.getcwd()}/new_images')
    list_of_processes = []
    number_of_processes = 2
    for x in range(number_of_processes):
        process = Process(target=process_images,
                          args=(list_of_new_images[x::number_of_processes],))
        process.start()
        list_of_processes.append(process)
    [process.join() for process in list_of_processes]


if __name__ == '__main__':
    main()