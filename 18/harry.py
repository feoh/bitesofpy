import os
import string
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    with open(harry_text,'r', encoding='utf-8') as hf:
        harry_string = hf.read()

    with open(stopwords_file,'r', encoding='utf-8') as sf:
        stopwords = sf.readlines()

    stopwords_stripped = [word.rstrip() for word in stopwords]
    stopwords = stopwords_stripped

    harry_words_raw = harry_string.split()
    harry_words_no_punct = [word.translate(word.maketrans('','',string.punctuation)) for word in harry_words_raw]
    harry_words_lower = [word.lower() for word in harry_words_no_punct]

    harry_words_no_stopwords = [word for word in harry_words_lower if word not in stopwords]
    harry_words_clean = [word for word in harry_words_no_stopwords if word.isalpha()]

    harry_counts = Counter(harry_words_clean)

    return harry_counts.most_common()[0]
