#========================Assignment:
'''
Create a class Employee with:
- a public variable name,
- a protected variable _salary, and
- a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.
'''

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name   # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn   # Private variable

employee = Employee("Zohaib", 52000, "4332-213-4343")

print("Public Name:", employee.name)  # Accessible
print("Protected Salary:", employee._salary)  # Accessible, but should be treated as protected
# print("Private SSN:", employee.__ssn)  # Raises AttributeError
print("Private SSN:", employee._Employee__ssn)  # Accessible using name mangling

# name mangling is a technique used in Python to make private variables more difficult to access from outside the class.