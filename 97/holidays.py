from collections import defaultdict
import os
from typing import Union
from urllib.request import urlretrieve

import bs4.element
from bs4 import BeautifulSoup, ResultSet, Tag, NavigableString
import html5lib
from datetime import datetime

# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def process_row(holiday_row) -> tuple:
    holiday_tds: ResultSet = holiday_row.find_all('td')
    date_str = holiday_tds[1].contents[1]['datetime']
    holiday_name = holiday_tds[3].text.strip()
    return date_str, holiday_name


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    sorted_holidays = []
    soup = BeautifulSoup(content, 'html5lib')
    holiday_table: bs4.element.Tag = soup.find('table','list-table')
    holiday_rows: ResultSet = holiday_table.find_all('tr', {'class': 'holiday'})
    regional_rows: ResultSet = holiday_table.find_all('tr', {'class': 'regional'})
    public_rows: ResultSet = holiday_table.find_all('tr', {'class': 'publicholiday'})
    all_rows: ResultSet = holiday_rows + regional_rows + public_rows
    holiday_row: bs4.element.Tag
    for holiday_row in all_rows:
        sorted_holidays.append(process_row(holiday_row))

    sorted_holidays.sort()

    for holiday in sorted_holidays:
        (yyyy, mm, dd) = holiday[0].split('-')
        holiday_name = holiday[1]
        holidays[mm].append(holiday_name)

    return holidays



