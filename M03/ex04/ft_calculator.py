class calculator:
    '''This calculator class that is able to do calculations
    (dot product, addition, subtraction) of 2 vectors.'''

    def __init__(self, v1: list[float], v2: list[float]):
        '''
        Init calculator's class
        '''
        self.V1 = v1
        self.V2 = v2

    # decorator
    
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        ''' decorator : addition of products of the list elements'''

        print("Dot product is:", sum([V1[i] * V2[i] for i in range(len(V1))]))

    # decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        ''' decorator : addition of 2 vectors'''

        print("Add Vector is:", [float(V1[i]) + float(V2[i])
                                 for i in range(len(V1))])

    # decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        ''' decorator : substraction of 2vectors'''

        print("Sous Vector is:", [float(V1[i]) - float(V2[i])
                                  for i in range(len(V1))])


# https://www.programiz.com/python-programming/decorator
# > Basically, a decorator takes in a function, adds some functionality and returns it.
# Cet exercice ne nous permet donc pas de faire des decorators
# (ou alors j'ai pas compris le prototype donne!)
