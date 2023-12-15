import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    '''
    Dataclass that takes as arguments a name and nickname, set active to True,
    create the student login, and generate a random ID with the generate_id function.
    You must not use __str__ , __repr__ in your class
    The login and id should not be initializable and must return an error.
    '''
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
#your code here
