"""5. Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time."""

bad_passwords = ["password", "letmein", "sesame","hello","justinbieber"]
while True:
    password_one = input("Enter your new password: ")

    if len(password_one) <8 or len(password_one) >12:
        print("Error! Password must be between 8 and 12 characters long. Try Again")

    elif password_one in bad_passwords:
        print("Error! Password is too common. Please choose a different password.")
    
    else:
        password_two = input("Re-enter your password: ")

        if password_one == password_two:
            print("Password Set Successfully!")

        else:
            print("Error! Password do not match. Try Again")

