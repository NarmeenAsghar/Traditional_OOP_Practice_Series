#===================Assignment:
'''
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
'''

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# in static method, we don't need to create an instance of the class to call the method
# we can call it directly using the class name
print(TemperatureConverter.celsius_to_fahrenheit(6))