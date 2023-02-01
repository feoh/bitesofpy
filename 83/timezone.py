from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt: datetime):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aware_oz_dt = AUSTRALIA.fromutc(naive_utc_dt)
    aware_sp_dt = SPAIN.fromutc(naive_utc_dt)
    return (aware_oz_dt, aware_sp_dt)

