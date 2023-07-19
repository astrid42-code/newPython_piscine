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
    img_format_w = img.size


    print("The shape of image is :", img_format_w)
    
    # prints mode of image
    print(img.mode)