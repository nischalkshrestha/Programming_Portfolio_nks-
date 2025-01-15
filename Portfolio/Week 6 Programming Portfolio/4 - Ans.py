"""Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way."""

def input_string():
    message= input("Enter any message: ")
    return message

message=input_string()

no_spaces=message.replace(" ","")
final_reverse=no_spaces[ ::-1]
final_reverse.lower
print(final_reverse)