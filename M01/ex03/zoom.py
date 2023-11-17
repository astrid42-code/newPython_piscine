import numpy as np
from load_image import ft_load
#import matplotlib.image as mpimg
import cv2
import matplotlib.pyplot as plt



# img = cv2.imread('animal.jpeg') # cv2.imread_grayscale('animal.jpeg', 0) pour passer en N&B?
# cf https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# plt.imshow(img)
# plt.show()
# img = img[...,: 3]
# plt.imshow(img)
# plt.show()

def ft_zoom(img) :

    px = np.zeros((400, 400, 1))

    y1, x1, z1 = px.shape

    for i in range(y1):
        
        for j in range(x1):
            r = img[i][j][0]
            g = img[i][j][2]
            b = img[i][j][1]
            grayscale = int(0.3 * r + 0.59 * g + 0.11 * b)
            px[i][j] = grayscale

    return (px.shape)
    

def main():
    img = cv2.imread('animal.jpeg') # cv2.imread_grayscale('animal.jpeg', 0) pour passer en N&B?
    print(ft_load("animal.jpeg"))
    
    beginY = 100
    endY = 500
    beginX = 450
    endX = 850
    # prevoir une gestion d erreur si tuple pas egal a 400, 400? et si hors cadre?
    # > la consigne voulant que le zoom soit sur une fenetre de 400 sur 400 dans l'image
    # + automatiser pour l user de pouvoir rentrer des coordonnees?
    tmp = img[beginY:endY, beginX:endX]
    px = cv2.cvtColor(img[beginY:endY, beginX:endX], cv2.COLOR_RGB2GRAY)

    res = ft_zoom(tmp)
    # print(ft_zoom(tmp))
    y1, x1 = px.shape
    print("New shape after slicing :", res, "or", tuple(px.shape[1::-1])) #https://stackoverflow.com/questions/19098104/python-opencv2-cv2-wrapper-to-get-image-size
    print(px)
    # pb dans affichage final et regler le tuple (400, 400, 1) 
    # > sans avoir besoin de faire la conversion dans ft_zoom
    # + tout mettre dans zoom??
    plt.imshow(px, cmap='gray') # tag cmap pour affichage NB avec plt
    # cf https://stackoverflow.com/questions/62855718/why-would-cv2-color-rgb2gray-and-cv2-color-bgr2gray-give-different-results
    plt.show()


if __name__ == "__main__":
    main()

# expected output
# python zoom.py
# The shape of image is: (768, 1024, 3)
# [[[120 111 132]
# [139 130 151]
# [155 146 167]
# ...
# [120 156 94]
# [119 154 90]
# [118 153 89]]]
# New shape after slicing: (400, 400, 1) or (400, 400)
# [[[167]
# [180]
# [194]
# ...
# [102]
# [104]
# [103]]]
