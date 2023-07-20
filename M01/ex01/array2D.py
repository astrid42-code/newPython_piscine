def slice_me(family: list, start: int, end: int) -> list:

    """
    This function that takes as parameters a 2D array,
    prints its shape, and returns a truncated version
    of the array based on the provided start and end arguments.
    """

    # gestion des erreurs :
    # verif du type :
    if type(family) != list:
        assert False, "this is not a list"
    # verifier que les lists de family font la meme taille

    i = 0

    while i < len(family) - 1:
        if len(family[i]) != len(family[i+1]):
            assert False, "the lists are not equal"
        i += 1
    count_h = i + 1
    count_w = len(family[0])
    newfamily = family[start:end]
    i = 0
    while i < len(newfamily) - 1:
        i += 1
    print("My shape is : (", count_h, ", ", count_w, ")", sep="")
    print("My new shape is : (", len(newfamily), ", ", count_w, ")", sep="")

    return (newfamily)
