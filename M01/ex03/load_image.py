import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def ft_load(path: str) -> array: # (you can return to the desired format)

    """
    This program should load the image "animal.jpeg", print some information
    about it and display it after "zooming".
    • The size in pixel on both X and Y axis
    • The number of channel > ???
    • The pixel content of the image.
    • Display the scale on the x and y axis on the image
    """

    img = mpimg.imread(path)
    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)
    print("The shape of image is :", img.shape)
    y,x,z = img.shape
    for i in range(y):
        for j in range(x):
            print(img[i, j])

    # plt.imshow(img)

    # plt.show()

# https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html
