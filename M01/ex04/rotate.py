from load_image import ft_load

def main():
    # img = cv2.imread('animal.jpeg') # cv2.imread_grayscale('animal.jpeg', 0) pour passer en N&B?
    print(ft_load("animal.jpeg"))


if __name__ == "__main__":
    main()


# Faire un tester.py (comme dans les autres exos)


# expected output:
# $> python rotate.py
# The shape of image is: (400, 400, 1) or (400, 400)
# [[[167]
# [180]
# [194]
# ...
# [102]
# [104]
# [103]]]
# New shape after Transpose: (400, 400)
# [[167 180 194 ... 64 50 72]
# ...
# [115 116 119 ... 102 104 103]
