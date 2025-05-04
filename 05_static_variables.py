#=========================Assignment:
'''
Create a class MathUtils with a static method add(a, b) that returns the sum. 
No class or instance variables should be used.
'''

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(2, 5))
print(MathUtils.add(10, 20))



print("=" * 80)


# ----------------Input from user----------------

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
    
sum = MathUtils.add(int(input("Enter first number: ")), int(input("Enter second number: ")))
print(f"Sum of two numbers is: {sum}")