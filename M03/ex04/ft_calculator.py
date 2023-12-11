class calculator:
    '''This calculator class that is able to do calculations
    (dot product, addition, subtraction) of 2 vectors.'''

    def __init__(self, v1: list[float], v2:list[float]):
        '''
        Init calculator's class
        '''
        self.V1 = v1
        self.V2 = v2
        
    # decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        ''' decorator : addition of products of the list elements'''


    # decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        ''' decorator : addition of 2 vectors'''

        print("Dot product is:", add())
    

    # decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        ''' decorator : substraction of 2vectors'''


    def __add__(self, object) -> None:
        ''' addition function : add a scalar value to instance's elements '''

        self.v = [i + object for i in self.v]  # comprehension list
        print(self.v)
    
    def __mul__(self, object) -> None:
        ''' multiplication function :
        multiply a scalar value to instance's elements '''

        self.v = [i * object for i in self.v]  # comprehension list
        print(self.v)

    def __sub__(self, object) -> None:
        ''' substraction function :
        substract a scalar value to instance's elements '''

        self.v = [i - object for i in self.v]  # comprehension list
        print(self.v)

    def __truediv__(self, object) -> None:
        ''' division function :
        divide a scalar value to instance's elements'''

        if object == 0:
            return print("ZeroDivisionError: float division by zero")
        self.v = [i / object for i in self.v]  # comprehension list
        print(self.v)


# https://www.programiz.com/python-programming/decorator
# > Basically, a decorator takes in a function, adds some functionality and returns it.
