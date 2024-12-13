"""3. Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur."""

def input_data():
    name = input("Please enter your name: ")
    return name
    
def check_name(name):
    if name == "":
        print("Hello, Stranger!")
    else:
        name = name[0].upper() + name[1:].lower()
        print("Hello,",name,".")

name = input_data()
check_name(name)


