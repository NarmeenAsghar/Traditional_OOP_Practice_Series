#-====================Assignment:
'''
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
'''

class Product:
    def __init__(self, price):  # constructor of Product class
        self._price = price
 
    @property # property decorator to define a getter method
    def price(self):  # this method is called when we access the price attribute
        return self._price

    @price.setter  # setter decorator to define a setter method
    def price(self, value):  # this method is called when we set the price attribute
        self._price = value

    @price.deleter  # deleter decorator to define a deleter method
    def price(self):  # this method is called when we delete the price attribute
        del self._price

p = Product(100)
print(p.price)
p.price = 150
print(p.price)
del p.price
