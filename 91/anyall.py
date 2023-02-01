VOWELS = 'aeiou'
PYTHON = 'python'
DIGITS = '0123456789'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return set(input_str.lower()).issubset(set(VOWELS))


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return bool([c for c in input_str.lower() if c in PYTHON])


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return bool([c for c in input_str if c in DIGITS])
