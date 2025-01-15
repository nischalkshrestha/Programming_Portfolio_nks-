"""Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']."""

def take_input():
    str=input("Enter any string: ")
    return str
str= take_input()


unique_letters= set(str)
print(sorted(unique_letters))

