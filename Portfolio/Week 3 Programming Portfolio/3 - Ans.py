"""3. Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long."""

password_one = input("Enter your password: ")

if len(password_one) <8 or len(password_one) >12:
    print("Error! Password must be between 8 and 12 characters long.")
else:
    password_two = input("Re-enter your password: ")

    if password_one == password_two:
        print("Password Set Successfully!")

    else:
        print("Error! Password do not match.")
