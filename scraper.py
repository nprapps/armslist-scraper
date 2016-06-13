#!/usr/bin/env python
import requests

from bs4 import BeautifulSoup
from collections import OrderedDict

ARMSLIST_URL = 'http://www.armslist.com/classifieds/search'

def scrape():
    param_arguments = [('location', 'florida'), ('category', 'all'), ('posttype', '7')]
    params = OrderedDict(param_arguments)
    response = requests.get(ARMSLIST_URL, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    container = soup.find(id='bootstrap-overrides')
    divs = container.find_all('div')
    for div in divs:
        href = div.get('href')
        if href:
            print(div)
        


if __name__ == '__main__':
    scrape()
