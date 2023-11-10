import numpy as np
from array import array
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.axis import Axis

# def binarise(tab, seuil, w, h):
#     """Cette fonction renvoie un tableau représentant l'image binarisée"""
#     for i in range (0,h,1) :
#         for j in range (0,w,1) :
#         #print(i,j)
#             if tab[i][j] >= seuil :
#                 tab[i][j] = 0
#             else :
#                 tab[i][j] = 1
#     return (tab)

def ft_error(path: str):
    str = path[-3:]
    str2 = path[-4:]
    # print(str, " ", str2)
    # incorrect format (ex jp au lieu de jpg)
    if (str != 'jpg' and str != 'peg' and str2 != 'jpeg' and str2 != '.jpg'):
        assert False, "Incorrect format / path"
    # incorrect path TODO!!
    print("coucou")


def ft_load(path: str) -> array:  # (you can return to the desired format)

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
    print("The shape of image is :", img.shape)
    y, x, z = img.shape

    print("y= ", y, "x= ", x, "z = ", z)

    # a decommenter pour affichage:
    for i in range(y):
        print(" i = ", i, " y = ", y)
        # for j in range(x):
        #     print(img) 
            # j += 1
        # i += 1
    # modif faite manuellement, a automatiser 
    # avec envoi des donnees par l'utilisateur? avec un input?

    # print( " img = ", img[0][1][2]) 
    beginY = 100
    endY = 500
    beginX = 450
    endX = 850
    px = img[beginY:endY, beginX:endX]

    y1, x1, z1 = px.shape

    # print("y1= ", y1, "x= ", x1, "z = ", z1)
    print("New shape after slicing :", px.shape)
    # print("cmap = ", px.cmap)

    # w = len(px[0])
    # h = len(px)
    # binarise(px, 127, w, h)

    r = px[0][0][0]
    g = px[0][0][1]
    b = px[0][0][2]

    grayscale = 0.3 * r + 0.59 * g + 0.11 * b

    print("grayscale = ", grayscale)

    # for i in range(y1):
    #     # print("px_i=",px)
    #     for j in range(x1):
    #         print(px)


    # print(px)
    # plt.imshow(px)
    # plt.imshow(img)

    # plt.show()

# https://yard.onl/sitelycee/cours/python/traitementdimageonrecuperelesdon.html

# penser a la fermeture du programme apres le .show()
