from S1E9 import Character


class Baratheon(Character):
    '''
Representing the Baratheon family.
    '''

    def __init__(self, name, is_alive=True):
        '''
        Init Stark's class
        '''
        # try:
        #     Character.__init__(self, name, is_alive)
        # except Exception as e:
        #     print(e)
        Character.__init__(self, name, is_alive)

    def die(self):
        '''
        method that passes is_alive from True to False
        '''
        # try:
        #     self.is_alive = not self.is_alive
        # except Exception as e:
        #     print(e)
        self.is_alive = False


class Lannister(Character):
    '''
Representing the Lannister family.
    '''
    def __init__(self, name, is_alive=True):
        '''
        Init Stark's class
        '''
        # try:
        #     Character.__init__(self, name, is_alive)
        # except Exception as e:
        #     print(e)
        Character.__init__(self, name, is_alive)

    def die(self):
        '''
        method that passes is_alive from True to False
        '''
        # try:
        #     self.is_alive = not self.is_alive
        # except Exception as e:
        #     print(e)
        self.is_alive = False

    #     # decorator
    # def create_lannister(your code here):
    #     '''
    #     Method to create characters in a chain
    #     '''
    #     #your code here


# __str__ et __repr__ :
# The __str__() and __repr__() methods can be helpful in debugging Python code by logging or printing useful information about an object
# https://www.digitalocean.com/community/tutorials/python-str-repr-functions
# https://www.docstring.fr/glossaire/str/
