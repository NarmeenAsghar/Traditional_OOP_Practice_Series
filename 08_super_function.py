#====================Assignment:
'''
Create a class Person with a constructor that sets the name. 
Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
'''

class Person:
    def __init__(self, name):  # constructor of Person class
        self.name = name

class Teacher(Person): # Teacher class inherits from Person class
    def __init__(self, name, subject):
        super().__init__(name)  # super calls the base class constructor means Person 
        self.subject = subject

teacher = Teacher("Waniya", "Math")
print(f"Teacher's Name: {teacher.name}")
print(f"Subject: {teacher.subject}")
