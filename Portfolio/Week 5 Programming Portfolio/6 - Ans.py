"""Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs."""

import sys
import shutil

if len(sys.argv) == 2:
    original_file = sys.argv[1]
    backup_file = original_file + "_backup"

    try:
        
        shutil.copy(original_file, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print(f"File '{original_file}' not found.")
else:
    print("Please provide a file name as an argument.")
