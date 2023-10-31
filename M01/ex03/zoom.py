from load_image import ft_load
#import matplotlib.image as mpimg
import cv2
import matplotlib.pyplot as plt


#print(ft_load("animal.jpeg"))

img = cv2.imread('animal.jpeg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(img)
#plt.show()
img = img[...,: 3]
plt.imshow(img)
plt.show()
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
