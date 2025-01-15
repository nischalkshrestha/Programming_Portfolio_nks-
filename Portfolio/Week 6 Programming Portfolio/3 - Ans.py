"""Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers."""

def user_input():
    number= int(input("Enter a number: "))
    return number
number=user_input()

if number<=1:
    print("It is not a prime number.")

else:  
    is_prime=True
    new_number=2
    while (new_number<number):
        if number%new_number==0:
            is_prime=False
        break
    new_number+=1

    if is_prime:
        print("It is a prime Number.")
    else:
        print("It is not a prime number.")
        

