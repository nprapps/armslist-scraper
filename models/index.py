from bs4 import BeautifulSoup
from dateutil.parser import parse

ARMSLIST_URL = 'http://www.armslist.com'

class IndexPage:
    def __init__(self, html, stop_datetime):
        """Makes global variables.

        The function recieves self, page html markup and configured date
        and assigns it to global variables within the class to be used. It also defines
        BeautifulSoup, makes an creates an empty list to hold scraped URLs and starts _parse function.
        """
        self._html = html
        self._stop_datetime = stop_datetime
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self.items = []
        self._parse()

    def _parse(self):
        """Targets URLs

        The function pulls the href for the listing divs and passes info to IndexItem class.
        It loops until a listing posted date surpasses the configured date.
        """
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
        """Assigning element to self._el variable to be used throughout class"""
        self._el = el

    @property
    def url(self):
        """Builds listing absolute URL

        The function combines the relative url from the post listing and domain name.
        """
        relative_url = self._el.get('href')
        if relative_url:
            return '{0}{1}'.format(ARMSLIST_URL, relative_url)

    @property
    def listing_date(self):
        """Formats listing date

        To target the date, function finds the second td due to pattern in code per listing,
        then finds the third div, which holds the date. From there, html is stripped to leave
        only date which is returned after being parsed.
        """
        second_td = self._el.find_all('td')[1]
        third_div = second_td.find_all('div')[2]
        junk, date_string = third_div.string.strip().split(', ')
        return parse(date_string)
