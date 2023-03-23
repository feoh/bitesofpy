import re
def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    match_spaces = re.match('^[ ]+',text)
    if match_spaces:
        matched_length = len(match_spaces[0])
        return matched_length
    else:
        return 0
