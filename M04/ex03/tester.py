from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

# Expected output: (id is random)
# Student(name='Edward', surname='agle', active=True,
#   login='Eagle', id='trannxhndgtolvh')

student = Student(name="Edward", surname="agle", id="toto")
print(student)

# Expected output:
# $> python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id
