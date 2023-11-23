import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# from matplotlib.axis import Axis
import cv2


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
    ft_error(path)

    img = mpimg.imread(path)

    # "assert img is not None" means your dataloader did not get your input data.
    # mais assert non pris en compte :(
    # assert img is not None, "file could not be read, check with os.path.exists()"

    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)

    x1, y1, z1 = img.shape

    # print(img)

    # phase 2 : zoom and gray change

    beginY = 100
    endY = 500
    beginX = 450
    endX = 850
    if (endY - beginY != 400 or endX - beginX != 400
       or beginY < 0 or beginX < 0 or endY > x1 or endX > y1):
        assert False, "coordinates are wrong"

    # + automatiser pour l user de pouvoir rentrer des coordonnees?

    px = cv2.cvtColor(img[beginY:endY, beginX:endX], cv2.COLOR_RGB2GRAY)
    tmp = np.reshape(px, (endY - beginY, endX - beginX, 1))

    print("The shape of image is :", tmp.shape, "or", px.shape)
    # tuple(px.shape[1::-1])) > https://stackoverflow.com/questions/19098104/python-opencv2-cv2-wrapper-to-get-image-size

    print(tmp) # (ou tmp)

    #  phase 3: rotate img 

    x2, y2 = px.shape

    # https://snakify.org/fr/lessons/two_dimensional_lists_arrays/ 
    res = [[i * j for j in range(y2)] for i in range(x2)]

    for x in range(x2):
        for y in range (y2):
            res[y][x] = px[x][y]
            # print("tmp = ", tmp[y][x], " px = ", px[x][y])

    res = np.reshape(res, (400, 400))
    print("New shape after Transpose is :", res.shape)
    print(res)

    plt.imshow(res, cmap='gray')  # tag cmap pour affichage NB avec plt
    # cf https://stackoverflow.com/questions/62855718/why-would-cv2-color-rgb2gray-and-cv2-color-bgr2gray-give-different-results
    plt.show()

# # # https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# # # penser a la fermeture du programme apres le .show()
