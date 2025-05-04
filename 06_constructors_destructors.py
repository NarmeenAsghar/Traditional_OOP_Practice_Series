#=======================Assignment:
'''
Create a class Logger that prints a message when an object is created (constructor) and another message 
when it is destroyed (destructor).
'''

# importing time module for better and clear result
import time

class Logger:
    def __init__(self):
        print("Logger object created.")  # when object is created this message will automatically print

    def __del__(self):
        print("Logger object destroyed.")  # when object is deleted or destroyed this message will automatically print

time.sleep(3)
logger = Logger()  # creating object

time.sleep(2)
del logger  # delete the object