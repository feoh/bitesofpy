import string
from collections import Counter, defaultdict
import csv
from typing import Dict, Any

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def cleanup_line(line: str):
    # Strip newline and remove punctuation.
    # line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    return line


def get_num_words_spoken_by_character_per_episode(content: str):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    lines_by_character: dict[str, Counter] = {}

    reader = csv.DictReader(content.splitlines())

    for row in reader:
        lines_by_character.setdefault(row['Character'], Counter())

        line = row['Line']

        line = cleanup_line(line)
        word_count = len(line.split())

        lines_by_character[row['Character']].update({row['Episode']: word_count})

    return lines_by_character
