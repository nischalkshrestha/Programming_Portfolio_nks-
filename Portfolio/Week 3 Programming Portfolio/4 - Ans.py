"""4. Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

bad_password = ["password", "letmein", "sesame","hello","justinbieber"]
password_one = input("Enter your new password: ")

if len(password_one) <8 or len(password_one) >12:
    print("Error! Password must be between 8 and 12 characters long.")

elif password_one in bad_password:
    print("Error! Password is too common. Please choose a different password.")
    
else:
    password_two = input("Re-enter your password: ")

    if password_one == password_two:
        print("Password Set Successfully!")

    else:
        print("Error! Password do not match.")

