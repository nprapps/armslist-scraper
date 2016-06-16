#!/usr/bin/env python
"""
Scrape a state's listings page to harvest listing links.
"""

import csv
import requests
import sys

from collections import OrderedDict
from datetime import datetime
from models.index import IndexPage
from utils import eprint

ARMSLIST_SEARCH_URL = 'http://www.armslist.com/classifieds/search'
STOP_DATETIME = datetime(2016, 3, 15, 0, 0, 0)
DEFAULT_QUERY_ARGUMENTS = [
    ('category', 'guns'),
    ('posttype', '3'),
    ('page', 1)
]


def scrape_index(state, stop_datetime):
    params = OrderedDict(DEFAULT_QUERY_ARGUMENTS)
    params['location'] = state
    writer = csv.writer(sys.stdout)

    while True:
        response = requests.get(ARMSLIST_SEARCH_URL, params=params)
        eprint('{0} [{1}]'.format(response.url, response.status_code))
        page = IndexPage(response.content, stop_datetime)
        if not len(page.items):
            break

        for item in page.items:
            writer.writerow([item.url, state, item.listing_date])

        params['page'] += 1


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('state name required')
        sys.exit()

    state = str(sys.argv[1])
    scrape_index(state=state, stop_datetime=STOP_DATETIME)
