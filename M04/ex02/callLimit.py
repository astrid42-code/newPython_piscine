def callLimit(limit: int):
    '''function that takes as argument a call limit of another function
    and blocks its execution above a limit.'''

    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):

            nonlocal count
            if count >= limit:
                # raise Exception(f"Error: ", function, "call too many times")
                print(f'Error: {function} call too many times')
            else:
                function()
            count += 1

        return limit_function
    return callLimiter


# Exemples de code decorators pour limites :
# https://zestedesavoir.com/forums/sujet/1346/exercice-python-les-decorateurs/
