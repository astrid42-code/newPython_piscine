from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''

    def __init__(self, name, is_alive=True):
        '''Init Stark's class'''

        Character.__init__(self, name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        '''The __str__() method returns a human-readable, or informal,
        string representation of an object. '''
        return f'Vector: (\'{self.family_name}\', {self.eyes}\',{self.hairs})'

    def __repr__(self):
        '''The __repr__() method returns a more information-rich,
        or official, string representation of an object.'''

        return f'Vector: (\'{self.family_name}\', {self.eyes}\',{self.hairs})'
        # return self.__str__()

    def die(self):
        '''method that passes is_alive from True to False'''

        self.is_alive = False


class Lannister(Character):
    '''Representing the Lannister family.'''

    def __init__(self, name, is_alive=True):
        '''Init Stark's class'''

        Character.__init__(self, name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        '''The __str__() method returns a human-readable, or informal,
        string representation of an object. '''
        return f'Vector: (\'{self.family_name}\', {self.eyes}\',{self.hairs})'

    def __repr__(self):
        '''The __repr__() method returns a more information-rich,
        or official, string representation of an object.'''
        
        return f'Vector: (\'{self.family_name}\', {self.eyes}\',{self.hairs})'
        # return self.__str__()

    def die(self):
        '''method that passes is_alive from True to False'''

        self.is_alive = False

        # decorator
    @classmethod
    def create_lannister(cls, name, is_alive=True):
        '''Method to create characters in a chain'''

        return cls(name, is_alive=True)


# __str__ et __repr__ :
# The __str__() and __repr__() methods can be helpful in debugging Python code by logging or printing useful information about an object
# https://www.digitalocean.com/community/tutorials/python-str-repr-functions
# https://www.docstring.fr/glossaire/str/

# @classmethod :
# syntax >
# @classmethod
# def func(cls, args...)
# https://www.programiz.com/python-programming/methods/built-in/classmethod
