from bs4 import BeautifulSoup
from dateutil.parser import parse

ARMSLIST_URL = 'http://www.armslist.com'

class IndexPage:
    def __init__(self, html, stop_datetime):
        self._html = html
        self._stop_datetime = stop_datetime
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self.items = []
        self._parse()

    def _parse(self):
        container = self._soup.find(id='bootstrap-overrides')
        if container:
            divs = container.find_all('div')
            for el in divs:
                href = el.get('href')
                if href:
                    item = IndexItem(el)
                    if item.listing_date < self._stop_datetime:
                        break
                    self.items.append(item)


class IndexItem:
    def __init__(self, el):
        self._el = el

    @property
    def url(self):
        relative_url = self._el.get('href')
        if relative_url:
            return '{0}{1}'.format(ARMSLIST_URL, relative_url)

    @property
    def listing_date(self):
        second_td = self._el.find_all('td')[1]
        third_div = second_td.find_all('div')[2]
        junk, date_string = third_div.string.strip().split(', ')
        return parse(date_string)
