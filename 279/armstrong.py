def is_armstrong(n: int) -> bool:
    n_string = str(n)
    n_digits = [int(digit) for digit in n_string]
    num_digits = len(n_digits)
    maybe_armstrong = sum([pow(digit, num_digits) for digit in n_digits])
    return maybe_armstrong == n
