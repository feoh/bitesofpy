def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """

    if n < 0:
        rot_chunk = string[n::]
        string = string.removesuffix(rot_chunk)
        string = rot_chunk + string
    elif n > 0:
        rot_chunk = string[:n:]
        string = string.removeprefix(rot_chunk)
        string = string + rot_chunk

    return string