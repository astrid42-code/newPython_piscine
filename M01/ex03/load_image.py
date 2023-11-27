import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# from matplotlib.axis import Axis
import cv2


def ft_load(path: str) -> array:  # (you can return to the desired format)

    # Refaire la docstring si necessaire
    """
    This program should load the image "animal.jpeg", print some information
    about it and display it after "zooming".
    • The size in pixel on both X and Y axis
    • The number of channel
    • The pixel content of the image.
    • Display the scale on the x and y axis on the image
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

    # "assert img is not None" means your dataloader did not get your input data.
    # mais assert non pris en compte :(
    # assert img is not None, "file could not be read, check with os.path.exists()"

    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)

    print("The shape of image is :", img.shape)

    x1, y1, z1 = img.shape

    print(img)

    # phase 2 : zoom and gray change

    beginY = 100
    endY = 500
    height = endY - beginY
    beginX = 450
    endX = 850
    width = endX - beginX
    if (endY - beginY != 400 or endX - beginX != 400
       or beginY < 0 or beginX < 0 or endY > x1 or endX > y1):
        assert False, "coordinates are wrong"

    # + automatiser pour l user de pouvoir rentrer des coordonnees?

    px = cv2.cvtColor(img[beginY:endY, beginX:endX], cv2.COLOR_RGB2GRAY)
    # tmp = np.reshape(px, (endY - beginY, endX - beginX, 1))
    # tmp = np.reshape(px, (height, width, 1))
    tmp = np.reshape(px, (height, width, 1))

    print("New shape after slicing :", tmp.shape, "or", px.shape)
    # tuple(px.shape[1::-1])) 
    # > https://stackoverflow.com/questions/19098104/python-opencv2-cv2-wrapper-to-get-image-size

    # print(px)
    print(tmp)

    # tag cmap pour affichage NB avec plt
    # # cf https://stackoverflow.com/questions/62855718/why-would-cv2-color-rgb2gray-and-cv2-color-bgr2gray-give-different-results
    plt.imshow(px, cmap='gray')  
    plt.show()


# # # https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# # # penser a la fermeture du programme apres le .show()
