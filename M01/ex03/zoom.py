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

def main():
    img = cv2.imread('animal.jpeg') # cv2.imread_grayscale('animal.jpeg', 0) pour passer en N&B?
    print(ft_load("animal.jpeg"))
    
    # print(img)
    # img = img[...,: 3]
    # plt.imshow(img)
    # plt.show()
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
