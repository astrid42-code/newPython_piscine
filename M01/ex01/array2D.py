import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

    """
    This function that takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """

    # gestion des erreurs : 
    # verifier que les lists de family font la meme taille
    i = 0
    j = 0
    print(family[i], " ", len(family[i]))
    # print(start, " , ", end)
    # while i < len(family):
    #     print(family[i])
    #     j = 0
    #     while j < len(family[i]):
    #         print(family[i][j])
    #         if (len(family[i][j]) != len(family[i+1][j])):
    #             assert False, "the lists are not equal"
    #         j += 1
    #     i += 1
    if type(family) != list:
        assert False, "this is not a list"
    
    count_h = 0
    count_w = 0
    i = 0
    # for i in family:

    # slice method :
    print(family[start:end])