"""The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string."""


import sys

def grep_command(search_string, file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if search_string in line:
                    print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep_command.py <search_string> <file_name>")
    else:
        search_string = sys.argv[1]
        file_name = sys.argv[2]
        grep_command(search_string, file_name)
