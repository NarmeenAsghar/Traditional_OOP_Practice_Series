#======================Assignment:
'''
Use the abc module to create an abstract class Shape with an abstract method area(). 
Inherit a class Rectangle that implements area()
'''
# The abc module provides tools for defining abstract base classes in Python.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # pass is used to indicate that this method is abstract and should be implemented by subclasses

class Rectangle(Shape):  # Rectangle class inherits from Shape class
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rectangle = Rectangle(5, 10)
print(f"Area of the rectangle: {rectangle.area()}")