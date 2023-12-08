from abc import ABC, abstractmethod

class Character(ABC):
    """
    This class takes a first_name as first parameter,
    is_alive as second non mandatory parameter set to True by default
    and can change the health state of the character 
    with a method that passes is_alive from True to False
    """
    
    @abstractmethod
    def __init__(self):
        self.is_alive = True
    
    def print_name(name):
        self.name = name
        print("Character's name is ", self.name)
    
    def is_it_alive(self):
        if self.is_alive is True:
            print(self.name, " is alive")
        else:
            print(self.name, " is truely dead. Winter is coming dude!")


class Stark(Character):
    """
    "stark" class inherits from Character's class
    """

    def __init__(name, is_alive):
        name = name
        is_alive = True

    def print_name(name):
        print("Stark's name is ", name)

    def is_it_alive(name, is_alive):
        if is_alive is True:
            print(name, " is alive")
        else:
            print(name, " is truely dead. Winter is coming dude!")


# https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours7_2021_slides.pdf
# Une classe abstraite est une classe qui ne permet pas d’instancier des objets.
# Elle ne peut servir que de modèle/d'interface pour les classes filles
# [...] une classe concrète doit re-définir toutes les méthodes abstraites.

# Attention : si on veut implementer une methode dans la classe abstraite
# sans avoir besoin de la redefinir dans les classes enfants (elle leur sera donc commune a toutes)
# il faut la mettre hors du scope @abstractmethod
# + self : appel a l'objet lui-meme
# https://he-arc.github.io/livre-python/abc/index.html


# comment faire pour is_alive qui est set as true by default ?
# le mettre dans init quand meme? si oui comment ? 
# si arg is_alive pas null (donc envoye dans le tester en param) le changer, sinon True ?
