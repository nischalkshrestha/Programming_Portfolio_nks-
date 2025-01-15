"""The Unix wc command counts the number of lines, words, and characters in a file.
Write an implementation of this that takes a file name as a command-line
argument, and then prints the number of lines and characters.
Note: Linux (and Mac) users can use the "wc" command to check the results of their
implementation."""

import sys

def wc_command(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_characters = sum(len(line) for line in lines)
            
            print(f"Lines: {num_lines}")
            print(f"Characters: {num_characters}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc_command.py <file_name>")
    else:
        file_name = sys.argv[1]
        wc_command(file_name)
