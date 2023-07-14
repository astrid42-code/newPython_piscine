def isNan(num):
    return num != num
# comparer un element undefined a lui meme, donnera deux valeurs differentes,
# donc renvoie false
# et le seul cas ou c possible c nan (car il n'y a pas de null pour un nb)


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
        return 0
    elif isNan(object):
        print("Cheese:", object, type(object))
        return 0
    elif object == 0:
        print("Zero:", object, type(object))
        return 0
    elif object == '':
        print("Empty:", object, type(object))
        return 0
    elif object is False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Type not Found")
        return 1

# ATTENTION : Running your function alone does nothing.
# Return 0 if it goes well and 1 in case of error. > ???
