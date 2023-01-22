puncts = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    clean = [ char for char in input_string if char not in puncts ]
    return clean
