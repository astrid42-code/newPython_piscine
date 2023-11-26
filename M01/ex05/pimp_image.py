from array import array
import numpy as np
import matplotlib.pyplot as plt
# import cv2

# You have some restriction operators for each function: (you can only use those given,
# you don’t have to use them all)


def ft_invert(array) -> array:
    # invert: =, +, -, *

    """
    Inverts the color of the image received
    """

    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for line in range(h):
        for col in range(w):
            for i in range(3):
                # print("res = ", res[l, c, i])
                res[line, col, i] = 255 - img[line, col, i]

    # print(res)

    plt.imshow(res)
    plt.show()

    return (res)


def ft_red(array) -> array:
    # red: =, *

    """
    Turns in red the image received
    """

    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for line in range(h):
        for col in range(w):
            # res[l, c] = 255
            for i in range(3):
                if (i != 0):
                    res[line, col, i] = 0

    # print(res)

    plt.imshow(res)
    plt.show()

    return (res)


def ft_green(array) -> array:
    # green: =, -

    """
    Turns in green the image received
    """
    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for line in range(h):
        for col in range(w):
            # res[l, c] = 255
            for i in range(3):
                if (i != 1):
                    res[line, col, i] = 0

    # print(res)

    plt.imshow(res)
    plt.show()

    return (res)


def ft_blue(array) -> array:
    # blue: =

    """
    Turns in blue the image received
    """
    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for line in range(h):
        for col in range(w):
            for i in range(3):
                if (i != 2):
                    res[line, col, i] = 0

    # print(res)

    plt.imshow(res)
    plt.show()

    return (res)


def ft_grey(array) -> array:
    # grey: =, /
    # https://www.baeldung.com/cs/convert-rgb-to-grayscale

    """
    Turns in grey the image received
    """
    img = np.asarray(array)
    h, w, _ = array.shape

    res = np.copy(img)
    for line in range(h):
        for col in range(w):
            # res[l, c] = 255
            for i in range(3):
                r = res[line, col, 0]
                g = res[line, col, 1]
                b = res[line, col, 2]

                # sauf qu'on n'a pas le droit a * ??!!
                res[line, col, i] = 0.3 * r + 0.59 * g + 0.11 * b

    # print(res)

    plt.imshow(res)
    plt.show()

    return (res)


# useless but mandatory...
def main():
    print("Hello 42!")


if __name__ == "__main__":
    main()


# https://www.delftstack.com/fr/howto/python/opencv-invert-image/#inverser-les-images-%c3%a0-laide-de-la-m%c3%a9thode-numpyinvert-en-python
# https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/manipulations-dimages-i
