from load_image import ft_load
from array import array
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

# You have some restriction operators for each function: (you can only use those given,
# you don’t have to use them all) > see 

def ft_invert(array) -> array:
    # invert: =, +, -, *

    """
    Inverts the color of the image received
    """

    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for l in range(h):
        for c in range(w):
            for i in range(3):
                # print("res = ", res[l, c, i])
                res[l, c, i] = 255 - img[l, c, i]

    # print(res)

    # plt.imshow(res)
    # plt.show()

    return(res)


def ft_red(array) -> array:
    # red: =, *

    """
    Turns in red the image received
    """

    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for l in range(h):
        for c in range(w):
            # res[l, c] = 255
            for i in range(3):
                if (i != 0):
                     res[l, c, i] = 0
                # > if i != 0 (donc != du premier index de mon rgb) je mets a 0 (il ne reste alors que le rouge)

    print(res)

    plt.imshow(res)
    plt.show()

    return(res)


def ft_green(array) -> array:
    # green: =, -

    """
    Turns in green the image received
    """

def ft_blue(array) -> array:
    # blue: =

    """
    Turns in blue the image received
    """

def ft_grey(array) -> array:
    # grey: =, /

    """
    Turns in grey the image received
    """


# useless but mandatory...
def main():
    print("Hello 42!")


if __name__ == "__main__":
    main()


# https://www.delftstack.com/fr/howto/python/opencv-invert-image/#inverser-les-images-%c3%a0-laide-de-la-m%c3%a9thode-numpyinvert-en-python
# https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/manipulations-dimages-i