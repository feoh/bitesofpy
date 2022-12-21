def removesuffix(suff, s):
    n = len(suff)
    return s[:n+1:]


def removeprefix(p,s):
    return s[len(p)::]


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """

    suffix = string[n::]
    prefix = string[0:n]
    rotated = suffix + prefix

    return rotated