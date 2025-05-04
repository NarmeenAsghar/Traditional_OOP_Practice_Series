#=================Assignment:
'''
Create a class Multiplier with an __init__() to set a factor. 
Define a __call__() method that multiplies an input by the factor. 
Test it with callable() and by calling the object like a function.
'''

class Multiplier:
    def __init__(self, factor):  # constructor of Multiplier class
        self.factor = factor

    def __call__(self, number):  # this method is called when the object is called like a function
        return self.factor * number

m = Multiplier(3)
print(callable(m)) 
print(m(10)) 