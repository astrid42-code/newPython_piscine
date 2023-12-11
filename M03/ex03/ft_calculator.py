class calculator:
    '''This class is able to do calculations
    (addition, multiplication, subtraction, division)
    of vector with a scalar'''

    def __init__(self, v: list):
        '''
        Init calculator's class
        '''
        self.v = v

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


# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
