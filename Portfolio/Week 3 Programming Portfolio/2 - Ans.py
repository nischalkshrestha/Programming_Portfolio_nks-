"""2. Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error."""

enterpass = input("Enter your password: ")
reenter_pass = input("Re-enter your password: ")
if enterpass == reenter_pass:
    print("Password Set Successfully!")
else:
    print("Error! Password do not match")
