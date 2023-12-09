from S1E9 import Stark


Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

# Expected output :
# {'first_name': 'Ned', 'is_alive': True}
# True
# False
# Your docstring for Class
# Your docstring for Constructor
# Your docstring for Method
# ---
# {'first_name': 'Lyanna', 'is_alive': False}

# TEST ERROR

from S1E9 import Character
hodor = Character("hodor")

# Expected output :
# TypeError: Can't instantiate abstract class Character with abstract method
