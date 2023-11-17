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
            # print("i = ", i, "px_i=",px[i][j], " j = ", j)
            # print("img_i=",img[i][j])
    
    # Si le résultat n'est pas un tableau d'entiers
    if img.dtype == np.float32:
        img = (img * 255).astype(np.uint8)

    print("New shape after slicing :", px.shape)
    return (px)
    

def main():
    img = cv2.imread('animal.jpeg') # cv2.imread_grayscale('animal.jpeg', 0) pour passer en N&B?
    print(ft_load("animal.jpeg"))
    
    beginY = 100
    endY = 500
    beginX = 450
    endX = 850
    px = img[beginY:endY, beginX:endX]

    print(ft_zoom(px))
    # print(img)
    # img = img[...,: 3]
    plt.imshow(px)
    plt.show()
    # img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # cv2.imshow('animal.jpeg', img2)
    # plt.imshow(img2)
    # plt.show()
    # gray = cv2.imread('animal.jpeg', cv2.IMREAD_GRAYSCALE)
    # plt.imshow(gray)
    # plt.show()

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
