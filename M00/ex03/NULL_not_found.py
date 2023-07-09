def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing:", object, type(object))
        return 0
    elif object == "nan": #pb dans la condition (Cheese: nan <class 'float'>)
        return 0
    elif object == 0:
        print("Zero:", object, type(object))
        return 0
    elif object == '':
        print("Empty:", object, type(object))
        return 0
    elif object == False:
        print("Fake:", object, type(object))
        return 0
    else:
        print("Cheese:", object, type(object))
        print("Type not Found")
        return 1


# float ne fctionne pas actuellement

# ATTENTION : Running your function alone does nothing.
# Return 0 if it goes well and 1 in case of error. > ???