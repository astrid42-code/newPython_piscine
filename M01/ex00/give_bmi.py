def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    """
    This function takes 2 lists of integers or floats
    in input and returns a list of BMI values.
    """

    # handling errors :
    # lists of same size
    if (len(height) != len(weight)):
        assert False, "the lists are not equal"
    # is it int or float
    i = 0
    while i < len(height):
        x = isinstance(height[i], int)
        y = isinstance(weight[i], int)
        if x != y:
            assert False, "the types are different"
        if height[i] == 0:
            assert False, "height can't be zero"
        i += 1

        # everything's ok :
    i = 0
    res = []
    while i < len(height):
        res += [weight[i] / (height[i] ** 2)]
        i += 1
    return (res)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """
    This function accepts a list of integers or floats
    and an integer representing a limit as parameters.
    It returns a list of booleans (True if above the limit).
    """

    i = 0
    res = []
    while i < len(bmi):
        if bmi[i] > limit:
            res += [True]
        else:
            res += [False]
        i += 1
    return res


# useless but mandatory...
def main():
    print("Hello 42!")


if __name__ == "__main__":
    main()
