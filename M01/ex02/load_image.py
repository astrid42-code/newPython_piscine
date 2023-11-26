import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def ft_load(path: str) -> array:  # (you can return to the desired format)

    """
    This function loads an image, prints its format, and its pixels
    content in RGB format. It can handle, at least, JPG and JPEG formats
    """

    # handling errors :
    # ft_error(str)
    # print(path.endswith(".jpg"))
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

    plt.imshow(img)

    plt.show()


# useless but mandatory...
def main():
    print("Hello 42!")


if __name__ == "__main__":
    main()


# https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# reste le None final a virer ...
# et la gestion d'erreur
