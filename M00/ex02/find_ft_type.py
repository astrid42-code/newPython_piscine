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
