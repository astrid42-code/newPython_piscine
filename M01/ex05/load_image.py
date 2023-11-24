import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# from matplotlib.axis import Axis
# import cv2


# a modifier (cf ex02)
def ft_error(path: str):
    str = path[-3:]
    str2 = path[-4:]
    # print(str, " ", str2)
    # incorrect format (ex jp au lieu de jpg)
    if (str != 'jpg' and str != 'peg' and str2 != 'jpeg' and str2 != '.jpg'):
        assert False, "Incorrect format / path"
    # incorrect path TODO!!
    # print("coucou")


def ft_load(path: str) -> array:  # (you can return to the desired format)

    """
    This function loads an image, prints its format, and its pixels
    content in RGB format. It can handle, at least, JPG and JPEG formats
    """

    # handling errors :
    # ft_error(str)

    img = mpimg.imread(path)

    # "assert img is not None" means
    # your dataloader did not get your input data.
    # mais assert non pris en compte :(
    # assert img is not None,
    # "file could not be read, check with os.path.exists()"

    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)

    print("The shape of image is :", img.shape)
    y, x, z = img.shape
    print(img)

    # plt.imshow(img)

    # plt.show()

    return(img)

# # # https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# # # penser a la fermeture du programme apres le .show()
