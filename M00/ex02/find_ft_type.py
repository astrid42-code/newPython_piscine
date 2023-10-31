"""def all_thing_is_obj(object: any) -> int:
    # print(type(object))
    if type(object) is list:
        print("List :", type(object))
    elif type(object) is tuple:
        print("Tuple :", type(object))
    elif type(object) is set:
        print("Set :", type(object))
    elif type(object) is dict:
        print("Dict :", type(object))
    elif type(object) is str:
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
        return 42"""
VALID_TYPES = [set, list, str, tuple, dict]


def all_thing_is_obj(object: any) -> int:
    type_obj = type(object)
    formated_obj = str(type_obj).split("'")[1].capitalize()
    if type_obj is str:
        print(f'{object} is in the kitchen : {type_obj}')
    else:
        print(f'{formated_obj} : {type_obj}' if type_obj in VALID_TYPES
              else "Type not found")
    return 42
