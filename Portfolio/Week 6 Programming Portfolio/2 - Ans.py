"""Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original)."""

def user_input():
    number=int(input("Enter an integer: "))
    return number

number= user_input()

for newnum in range(1,number+1):
    if number%newnum==0:
        print(newnum)


        
