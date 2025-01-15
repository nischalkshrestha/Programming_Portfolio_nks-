"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do."""

import sys

args = sys.argv[1:]

if args:
    
    shortest_arg = sorted(args, key=len)[0]
    print(f"The shortest argument is: {shortest_arg}")
else:
    print("No arguments were provided.")
