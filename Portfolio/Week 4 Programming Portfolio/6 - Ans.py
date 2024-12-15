"""6. Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperature = input("Enter temperature in Celsius: ")

if temperature[-1].upper() == 'C':
    celsius = float(temperature[:-1])
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(fahrenheit,"F")  
else:
    print("Error! Please provide the value followed by 'c' in the correct format.")
