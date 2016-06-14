#!/usr/bin/env python

import sys
import requests

from models.listing import Listing

def scrape_listing(url):
    response = requests.get(url)
    listing = Listing(response.content)
    print('Title: ' + listing.title)
    print('Price: ' + listing.price)
    # print(listing.imgs)
    print('Location: ' + listing.location)
    print('Description: ' + listing.description)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('url required')
        sys.exit()

    url = str(sys.argv[1])
    scrape_listing(url=url)
