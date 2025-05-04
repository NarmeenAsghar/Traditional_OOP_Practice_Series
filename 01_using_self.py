#==============================Assignment:
'''
Create a class Student with attributes name and marks. 
Use the self keyword to initialize these values via a constructor. 
Add a method display() that prints student details.
'''

class Student:
# __init__ is a special method that initializes the object when it is created.
    def __init__(self, name, marks):  # constructor (self is a reference to the current instance of the class)
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} your total marks in English are {self.marks}.")

student = Student("Wasif", 265)
student.display()



print("=" * 80)


# ----------------Input from user----------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} \nTotal Marks: {self.marks}")

name = input("Enter name of Student: ")
marks = int(input("Enter marks of Student: "))

student = Student(name, marks)
student.display()