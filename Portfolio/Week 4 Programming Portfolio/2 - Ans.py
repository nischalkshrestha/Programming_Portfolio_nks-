"""2. Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program."""

def case(string):

    uppercase_num = 0
    lowercase_num = 0
    
    for character in string:
        if 'A' <= character <= 'Z':
            uppercase_num += 1
        elif 'a' <= character <= 'z':
            lowercase_num += 1
    
    return uppercase_num, lowercase_num


print("The number of uppercase and lowercase in the given string is: ")
print("(Uppercase, Lowercase) =",case("ArthuR"))
print("(Uppercase, Lowercase) =",case("NaMaStE NePaL"))