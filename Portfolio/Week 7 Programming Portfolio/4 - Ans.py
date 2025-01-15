"""One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes."""


from collections import Counter

def frequency_analysis(message):
    # Convert the message to lowercase and filter only alphabetic characters
    message = message.lower()
    letters_only = [char for char in message if char.isalpha()]

    # Count the frequency of each letter
    letter_counts = Counter(letters_only)

    # Find the six most common letters
    most_common_letters = letter_counts.most_common(6)

    # Display the results
    print("The six most common letters are:")
    for letter, count in most_common_letters:
        print(f"{letter}: {count} times")

# Example usage
message = input("Enter the encrypted message: ")
frequency_analysis(message)
