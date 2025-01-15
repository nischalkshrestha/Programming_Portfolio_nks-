"""Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both."""


def letters_in_at_least_one(word1, word2):
    """Returns a sorted list of letters that appear in at least one of the two words."""
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    """Returns a sorted list of letters that appear in both words."""
    return sorted(set(word1) & set(word2))

def letters_in_either_but_not_both(word1, word2):
    """Returns a sorted list of letters that appear in either word, but not in both."""
    return sorted(set(word1) ^ set(word2))


def test_functions():
    word1 = "hello"
    word2 = "world"

    print("Letters in at least one of the words:", letters_in_at_least_one(word1, word2))
    print("Letters in both words:", letters_in_both(word1, word2))
    print("Letters in either word, but not in both:", letters_in_either_but_not_both(word1, word2))


test_functions()
