"""Write a program that, when run from the command line, reports how many
arguments were provided."""

import sys

num_args = len(sys.argv) - 1

print(f"Number of arguments provided: {num_args}")
