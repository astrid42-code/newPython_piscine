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
    elif object is False:
        print("Fake:", object, type(object))
        return 0
    elif object == 0:
        print("Zero:", object, type(object))
        return 0
    elif object == '':
        print("Empty:", object, type(object))
        return 0
    else:
        print("Type not Found")
    return 1


# VALID_TYPES = [None, float, int, str, bool]

# def NULL_not_found(object: any) -> int:
#     type_obj = type(object)
#     formated_obj = str(type_obj).split("'")[1].capitalize()
#     # if type_obj is float:
#     #     print(f'{formated_obj} : {type_obj}' )
#     # else:
#     print(f' : {object} {type_obj}' if type_obj in VALID_TYPES
#             else "Type not found")
#     return 1

# ATTENTION : Running your function alone does nothing.
# code a moduler comme ex02?
