#==================Assignment:
'''
Create a class decorator add_greeting that modifies a class to add a 
greet() method returning "Hello from Decorator!". Apply it to a class Person.
'''

def add_greeting(cls): # class decorator 
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # add greet method to the class
    return cls

@add_greeting  # apply the class decorator to Person class
class Person:
    pass  # empty class

p = Person()
print(p.greet())