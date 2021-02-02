"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def strip_nonalpha(string):
    strip_filter = filter(str.isalpha, string)
    return "".join(strip_filter)


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    stripped_word = strip_nonalpha(word)
    lowered_word = stripped_word.lower()
    reversed_word = lowered_word[::-1]

    return lowered_word == reversed_word


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""

    if not words:
        words = load_dictionary()
    palindromic_words = [word for word in words if is_palindrome(word)]
    palindromic_words.sort(key=len)
    longest = palindromic_words[-1]
    return longest