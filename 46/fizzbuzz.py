from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num % 3 == 0:
        return "fuzz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num