from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Representing the King family.'''

    def __str__(self):
        '''The __str__() method returns a human-readable, or informal,
        string representation of an object. '''

        return f'Vector: (\'{self.family_name}\', {self.eyes}\',{self.hairs})'

    def __repr__(self):
        '''The __repr__() method returns a more information-rich,
        or official, string representation of an object.'''

        return f'Vector: (\'{self.family_name}\', {self.eyes}\',{self.hairs})'
        # return self.__str__()

    def set_eyes(self, color: str):
        '''Setter function'''

        self.eyes = color

    def set_hairs(self, color: str):
        '''Setter function'''

        self.hairs = color

    def get_eyes(self):
        '''Getter function'''

        return (self.eyes)

    def get_hairs(self):
        '''Getter function'''

        return (self.hairs)

    def die(self):
        '''method that passes is_alive from True to False'''

        self.is_alive = False

# pas d'init car herite de ses deux parents(?)
# If you call the method m on an instance x of D, i.e. x.m(), we will get the output "m of B called". If we transpose the order of the classes in the class header of D in "class D(C,B):", we will get the output "m of C called".
# https://python-course.eu/oop/multiple-inheritance.php
# > l'ordre des classes parents dans le petit-enfant determine l'heritage (premiere classe parent)
# (a quoi sert la deuxieme donc?)