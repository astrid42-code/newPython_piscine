import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''generate randomly an ID for each user'''

    return ("".join(random.choices(string.ascii_lowercase, k=15)))


@dataclass
class Student:
    '''Dataclass that takes as arguments a name and nickname,
    set active to True, create the student login,
    and generate a random ID with the generate_id function.
    You must not use __str__ , __repr__ in your class
    The login and id should not be initializable and must return an error.'''

    # handling error a faire :
    # le login et l id ne peuvent pas etre initilise
    # dans les args envoyes a l instanciation de la classe
    # cf 2eme test du tester

    name: str
    surname: str
    active: bool = True

    login: str = field(init=False)
    id: str = field(init=False)
    # init=False
    # > The login and id should not be initializable and must return an error.

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname}"
        self.id = generate_id()

    def __format__(self, format_spec):
        if format_spec == "":
            return f"Student(name='{self.name}', surname='{self.surname}')"
        else:
            return f"Student(name='{self.name}', surname='{self.surname}'\
                             , active={self.active}, login='{self.login()}'\
                             , id={self,id}')"

    # pratique mais interdit :
    # def __repr__(self):
    #     return f"Student(name={self.name}, surname={self.surname}, active={self.active}, login={self.login}, id={self.id})"


# def dataclass (merci Bard)
# Les dataclasses sont conçues pour être utilisées pour représenter des données simples,
# telles que les points, les rectangles, les personnes, etc.
# Elles sont particulièrement utiles pour les données
# qui doivent être stockées dans une base de données ou échangées avec d autres systèmes.
# [en resume : avec le tag @dataclass, init et autres seront faits par defaut,
# sauf si je les definis avant]
