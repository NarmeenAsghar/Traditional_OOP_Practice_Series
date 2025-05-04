#===============================Assignment:
'''
Create a class Car with a public variable brand and a public method start(). 
Instantiate the class and access both from outside the class.
'''

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The one of the best car {self.brand} is launched.")

car = Car("Audi")
print(car.brand)
car.start()



print("=" * 80)


# ----------------Input from user----------------
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The one of the best car {self.brand} is launched.")

brand = input("Enter the brand of the car: ")

car = Car(brand)
print(car.brand)
car.start()