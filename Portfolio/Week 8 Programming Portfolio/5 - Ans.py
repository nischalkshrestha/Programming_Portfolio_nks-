"""The Unix spell command is a simple spell-checker. It prints out all the words in a
text file that are not found in a dictionary. Write and test an implementation of this,
that takes a file name as a command-line argument.
Note: You may want to simplify the program at first by testing with a text file that
does not contain any punctuation. A complete version should obviously be able to
handle normal files, with punctuation.
Another Note: You will need a list of valid words. Linux users will already have one
(probably in /usr/share/dict/words). It is more complicated, as usual, for
Windows users. Happily, there are several available on GitHub."""

import sys

def load_dictionary(dictionary_file):
    try:
        with open(dictionary_file, 'r') as file:
            # Read all valid words and store them in a set for fast lookup
            return set(word.strip().lower() for word in file)
    except FileNotFoundError:
        print(f"Error: The dictionary file '{dictionary_file}' was not found.")
        sys.exit(1)

def spell_check(file_name, dictionary):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.split()  # Split line into words based on whitespace
                for word in words:
                    clean_word = word.strip().lower()  # Normalize words
                    if clean_word not in dictionary:
                        print(f"Unknown word at line {line_number}: {clean_word}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell_command.py <file_to_check> <dictionary_file>")
    else:
        file_to_check = sys.argv[1]
        dictionary_file = sys.argv[2]
        
        dictionary = load_dictionary(dictionary_file)
        spell_check(file_to_check, dictionary)
