"""The Unix diff command compares two files and reports the differences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)"""

import sys

def diff_command(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

            if file1_lines == file2_lines:
                print("The files are the same.")
            else:
                print("The files are different.")
                
                # To show the differences line by line
                for line_num, (line1, line2) in enumerate(zip(file1_lines, file2_lines), start=1):
                    if line1 != line2:
                        print(f"Difference at line {line_num}:")
                        print(f"< {line1.strip()}")
                        print(f"> {line2.strip()}")

                # If one file is longer than the other, print the extra lines
                if len(file1_lines) > len(file2_lines):
                    print(f"\nFile '{file1}' has extra lines starting at line {len(file2_lines) + 1}:")
                    for extra_line in file1_lines[len(file2_lines):]:
                        print(f"< {extra_line.strip()}")
                elif len(file2_lines) > len(file1_lines):
                    print(f"\nFile '{file2}' has extra lines starting at line {len(file1_lines) + 1}:")
                    for extra_line in file2_lines[len(file1_lines):]:
                        print(f"> {extra_line.strip()}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_command.py <file1> <file2>")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        diff_command(file1, file2)
