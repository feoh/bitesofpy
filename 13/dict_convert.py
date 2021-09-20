from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code bChallenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

BlogNT = namedtuple("BlogNT", blog)


def dict2nt(dict_):
    return BlogNT(**blog)


def nt2json(nt):
    nt_dict = nt._asdict()
    return json.dumps(nt_dict, default=str)
