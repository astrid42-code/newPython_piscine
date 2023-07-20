import numpy as np
from array import array
import matplotlib.image as mpimg


def ft_load(path: str) -> array:  # (you can return to the desired format)

    """
    This function loads an image, prints its format, and its pixels
    content in RGB format. It can handle, at least, JPG and JPEG formats
    """

    # gestion d'erreurs a faire :
    # si path incorrect (ex : h.jpg) ou format incorrect (ex jp au lieu de jpg)

    img = mpimg.imread(path)
    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)
    print("The shape of image is :", img.shape)
    y, x, z = img.shape
    for i in range(y):
        for j in range(x):
            print(img[i, j])

    # plt.imshow(img)

    # plt.show()

# https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# reste le None final a virer ...
# et les [[]] au debut et a la fin
# et la gestion d'erreur
