from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'
ONE_DAY = 60 * 60 * 24

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    today = get_today()
    start_time = time()
    yield
    end_time = time()
    delta = end_time - start_time
    if delta > OPERATION_THRESHOLD_IN_SECONDS:
        violations[today] += 1
        if violations[today] >= ALERT_THRESHOLD:
            print(ALERT_MSG)

