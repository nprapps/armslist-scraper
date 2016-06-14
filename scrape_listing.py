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
    # print('Title: ' + listing.title)
    # print('Price: ' + listing.price)
    # print('Image URLs: ' + listing.imgs)
    # print('Location: ' + listing.location)
    # print('Description: ' + listing.description)
    # print('Category: ' + listing.category)
    # print('Manufacturer: ' + listing.manufacturer)
    # print('Caliber: ' + listing.caliber)
    # print('Action: ' + listing.action)
    # print('Firearm Type: ' + listing.firearm_type)
    # print('Listing Date: ' + listing.listed_date)
    # print('Post ID: ' + listing.post_id)
    # print('Registration: ' + str(listing.registered))
    # print('Party Type: ' + listing.party)
    writer.writerow([
        listing.post_id,
        listing.title,
        listing.listed_date,
        listing.price,
        listing.location,
        listing.description,
        listing.registered,
        listing.category,
        listing.manufacturer,
        listing.caliber,
        listing.action,
        listing.firearm_type,
        listing.party,
        listing.imgs
    ])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('url required')
        sys.exit()

    url = str(sys.argv[1])
    scrape_listing(url=url)
