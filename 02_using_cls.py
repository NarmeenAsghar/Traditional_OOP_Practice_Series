#==================--Assignment:
'''
Create a class Counter that keeps track of how many objects have been created. 
Use a class variable and a class method with cls to manage and display the count.
'''

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
# @classmethod is used to define a method that belongs to the class rather than an instance of the class.
    @classmethod
    def display(cls):  # cls stands for class and it is a convention to use.
        print(f"Number of objects that have been created: {cls.count}")

# creating objects
count_01 = Counter() 
count_02 = Counter()
count_03 = Counter()

Counter.display()