from load_image import ft_load


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()


# expected output :
# $> python tester.py
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
# $>
