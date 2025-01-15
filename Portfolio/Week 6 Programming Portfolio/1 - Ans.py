"""Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2)."""

def decimal_to_binary(number):
    binary_string = ''
    
    
    while number > 0:
        remainder = number % 2
        binary_string = str(remainder) + binary_string
        number = number // 2
    
    return binary_string


number = int(input("Enter a positive integer: "))


print("Binary representation:", decimal_to_binary(number))

