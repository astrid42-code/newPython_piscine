import numpy as np
from array import array
# from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def ft_load(path: str) -> array: # (you can return to the desired format)

    """
    This function loads an image, prints its format, and its pixels
    content in RGB format. It can handle, at least, JPG and JPEG formats
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

# reste le None final a virer ...