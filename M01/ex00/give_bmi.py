import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    """
    This function takes 2 lists of integers or floats in input and returns
    a list of BMI values.
    """
    
    # gestion des erreurs : 
    # verifier que les deux lists font la meme taille
    if (len(height) != len(weight)):
        assert False, "the lists are not equal"
    # est ce bien int ou float, si oui, les deux sont ils ints ou floats?
    
    # height ne peut pas etre egal a 0 (division par 0 est impossible)

    # si tout est ok :
    i = 0
    res = []
    while i < len(height):
        res += [weight[i] / (height[i] ** 2)]
        i += 1
    return (res)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """
    This function accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans (True if above the limit).
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

# def main():
#     if (len(sys.argv) != 1)
#         assert False, "ERROR: wrong number of arguments."
#     height = sys.argv[1]
#     w = sys.argv[2]


# if __name__ == "__main__":
#     main()


# IMC/BMI = weight / (height)^2