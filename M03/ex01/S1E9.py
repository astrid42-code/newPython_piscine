from abc import ABC, abstractmethod


class Character(ABC):
    """
    This class takes a first_name as first parameter,
    is_alive as second non mandatory parameter set to True by default
    and can change the health state of the character
    with a method that passes is_alive from True to False
    """

    def __init__(self, name, is_alive=True):
        '''
        Init Character's class
        '''

        self.name = name
        self.is_alive = is_alive
        
    @abstractmethod
    def die(self):
        '''
        method checking if is the character alive
        '''
        pass


class Stark(Character):
    """
    "stark" class inherits from Character's class
    """

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
        

# https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours7_2021_slides.pdf
# Une classe abstraite est une classe qui ne permet pas d’instancier des objets.
# Elle ne peut servir que de modèle/d'interface pour les classes filles
# [...] une classe concrète doit re-définir toutes les méthodes abstraites.

# Attention : si on veut implementer une methode dans la classe abstraite
# sans avoir besoin de la redefinir dans les classes enfants (elle leur sera donc commune a toutes)
# il faut la mettre hors du scope @abstractmethod
# + self : appel a l'objet lui-meme
# https://he-arc.github.io/livre-python/abc/index.html
