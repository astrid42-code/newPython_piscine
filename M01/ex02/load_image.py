import numpy as np
from array import array
from PIL import Image

def ft_load(path: str) -> array: # (you can return to the desired format)

    """
    This function loads an image, prints its format, and its pixels
    content in RGB format. It can handle, at least, JPG and JPEG formats
    """

    img = Image.open(path)
    img.load()
    # img.show()
    # prints format of image
    # print(img.format)
    img_h = img.size[0]
    img_w = img.size[1]


    print("The shape of image is :", img_w, img_h)
    pix_val = list(img.getdata())
    # print(type(pix_val))
    print(pix_val, sep='\n')

    
    # > imprime en tuple, pas en list
    # et ne va pas a la ligne

    # et la CA ME SAOULE GAVE!!!

    # prints mode of image
    # print(img.mode)