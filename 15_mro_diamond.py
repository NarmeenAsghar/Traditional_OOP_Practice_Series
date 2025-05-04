#===================Assignment:
'''
Create four classes:
- with a method show(),
- and C that inherit from A and override show(),
- that inherits from both B and C.
Create an object of D and call show() to observe MRO.
'''

# MRO (Method Resolution Order) is used to determine the order in which classes are searched when calling a method.
# MRO is used left-to-right, depth-first, and it is also used to resolve the diamond problem in multiple inheritance.
# The diamond problem occurs when a class inherits from two classes that both inherit from a common base class.


class A:  # Base class
    def show(self):
        print("A")

class B(A):  # Inherits from A
    def show(self):
        print("B")

class C(A):  # Inherits from A
    def show(self):
        print("C")

class D(B, C):  # Inherits from B and C
    pass

d = D()
d.show()

