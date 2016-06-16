#!/usr/bin/env python

import sys
import requests
import unicodecsv as csv

from models.listing import Listing
from utils import eprint


def scrape_listing(url):
    eprint(url)
    writer = csv.writer(sys.stdout)
    response = requests.get(url)
    listing = Listing(response.content)
    writer.writerow([
        url,
        listing.post_id,
        listing.title,
        listing.listed_date,
        listing.price,
        listing.location,
        listing.city,
        listing.state,
        listing.description,
        listing.registered,
        listing.category,
        listing.manufacturer,
        listing.caliber,
        listing.action,
        listing.firearm_type,
        listing.party,
        listing.img
    ])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('url required')
        sys.exit()

    url = str(sys.argv[1])
    scrape_listing(url=url)
