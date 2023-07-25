import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.axis import Axis


def ft_load(path: str) -> array:  # (you can return to the desired format)

    """
    This program should load the image "animal.jpeg", print some information
    about it and display it after "zooming".
    • The size in pixel on both X and Y axis
    • The number of channel > ???
    • The pixel content of the image.
    • Display the scale on the x and y axis on the image
    """

    img = mpimg.imread(path)
    assert img is not None, "file could not be read, check with os.path.exists()"
    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)
    print("The shape of image is :", img.shape)
    y, x, z = img.shape

    # print("y= ", y, "x= ", x, "z = ", z)

    # a decommenter pour affichage:
    # for i in range(y):
    #     for j in range(x):
    #         print(img) 

    # modif faite manuellement, a automatiser avec envoi des donnees par l'utilisateur? avec un input?

    beginY = 100
    endY = 500
    beginX = 450
    endX = 850
    px = img[beginY:endY, beginX:endX]


    y1, x1, z1 = px.shape

    # print("y1= ", y1, "x= ", x1, "z = ", z1)
    print("New shape after slicing :", px.shape)
    
    for i in range(y1):
        # print("px_i=",px)
        for j in range(x1):
            print(px) 

    # print(px)
    # plt.imshow(px)
    # plt.imshow(img)

    # plt.show()

# https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html
