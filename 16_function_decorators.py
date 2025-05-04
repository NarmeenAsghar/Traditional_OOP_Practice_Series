#====================Assignment:
'''
Write a decorator function log_function_call that prints "Function is being called" before a function executes. 
Apply it to a function say_hello().
'''

def log_function_call(func):
    def wrapper():  # wrapper function
        print("Function is being called")
        func()  # call the original function
    return wrapper

@log_function_call  # decorator syntax
def say_hello():
    print("Hello!")

say_hello()
