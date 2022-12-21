from datetime import datetime, timedelta


PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    perpetual_100_days_forward = PYBITES_BORN
    while True:
        perpetual_100_days_forward = perpetual_100_days_forward + timedelta(days=100)
        yield perpetual_100_days_forward
