def square(x: int | float) -> int | float:
    '''Function that returns the square of argument'''

    return (x * x)


def pow(x: int | float) -> int | float:
    '''function that returns the Exponentiation of argument by himself'''

    return (x ** x)


def outer(x: int | float, function) -> object:
    '''function that takes as argument a number and a function,
    it returns an object that when called returns the result
    of the arguments calculation
    '''

    count = 0

    def inner() -> float:
        nonlocal count
        if count != 0:
            count = function(count)
        else:
            count = function(x)
        return (count)
    return inner

# Inner functions are used so that they can be protected from everything
# happening outside the function. This process is also known as Encapsulation.
# https://www.geeksforgeeks.org/python-inner-functions/
