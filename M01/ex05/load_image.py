import numpy as np
from array import array
import matplotlib.image as mpimg
# from matplotlib.axis import Axis
# import cv2


def ft_load(path: str) -> array:  # (you can return to the desired format)

    """
    This function loads an image, prints its format, and its pixels
    content in RGB format. It can handle, at least, JPG and JPEG formats
    """

    # handling errors :
    if (path.endswith(".jpg") is False) and (path.endswith(".jpeg") is False):
        assert False, "Incorrect format / path"
    try:
        file = open(path)
        file.close()
    except Exception:
        assert False, "Unknown path"

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

    return (img)

# # # https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# # # penser a la fermeture du programme apres le .show()
