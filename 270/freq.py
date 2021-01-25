from collections import Counter


def freq_digit(num: int) -> int:
    digit_string = str(num)
    digit_counter = Counter(digit_string)
    most_frequent_digit = digit_counter.most_common()[0][0]
    return int(most_frequent_digit)