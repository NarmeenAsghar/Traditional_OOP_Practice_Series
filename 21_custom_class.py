#=====================Assignment:
'''
Create a class Countdown that takes a start number. 
Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
'''

class Countdown:
    def __init__(self, start):
        self.current = start  # initialize current to start number

    def __iter__(self):  # this method is called when the object is iterated
        return self

    def __next__(self):  # this method is called to get the next value in the iteration
        if self.current < 0:  # if current is less than 0, we stop the iteration
            raise StopIteration  # stop the iteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)