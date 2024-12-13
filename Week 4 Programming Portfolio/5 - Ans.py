"""5. Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("The Fahrenheit value is: ", fahrenheit)
    print()

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print("The Celsius value is: ", celsius)
    print()

def menu():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

boolean = True
while boolean:
    menu()  
    temperature = int(input("Enter the number from menu to do the operation: "))

    if temperature == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        celsius_to_fahrenheit(celsius)
    elif temperature == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        fahrenheit_to_celsius(fahrenheit)
    else:
        print("Invalid input!")
        boolean = False
