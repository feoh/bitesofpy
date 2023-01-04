import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as dfile:
        unstripped = dfile.readlines()
        return [ word.strip() for word in unstripped ]

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    word_letter_scores = [ LETTER_SCORES[letter.upper()] for letter in word if letter.upper() in LETTER_SCORES.keys() ]
    return sum(word_letter_scores)



def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    highest_scoring_word = ""

    for word in words:
        if calc_word_value(word) > calc_word_value(highest_scoring_word):
            highest_scoring_word = word
    
    return highest_scoring_word
