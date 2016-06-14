from bs4 import BeautifulSoup

class Listing:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self._characteristics = self._soup.find('ul', {'class': 'category'}).find_all('li')
        self._post_meta = self._soup.find('div', {'class': 'info-time'})

    @property
    def title(self):
        return self._soup.find('h1').string.strip()

    @property
    def price(self):
        span_contents = self._soup.find('span', {'class': 'price'})
        junk, price = span_contents.string.strip().split('$ ')
        return price

    @property
    def imgs(self):
        image_tags = self._soup.find_all('img', {'class': 'gallery'}) # have to sort out repeats
        for image_tag in image_tags:
            image_url = image_tag['src']
            return image_url

    @property
    def location(self):
        location_ul = self._soup.find('ul', {'class': 'location'})
        location_div = location_ul.find_all('div')[1]
        return location_div.text.strip()

    @property
    def description(self):
        desc = self._soup.find('div', {'class': 'postContent'})
        return desc.text.strip()

    @property
    def category(self):
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'category':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def manufacturer(self):
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'manufacturer':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def caliber(self):
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'caliber':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def action(self):
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'action':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def firearm_type(self):
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'firearm type':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def listed_date(self):
        return self._post_meta.find('span', {'class': 'date'}).text.strip()

    @property
    def post_id(self):
        return self._post_meta.find('span', {'class': 'user-id'}).text.strip().split(':  ')[1]

    @property
    def registered(self):
        info_div = self._soup.find('div', {'class': 'info-holder'})
        time_tag = info_div.find('time')
        if time_tag:
            time_tag = True
        else:
            time_tag = False
        return time_tag
        # returns if unregistered or registered and date
        # if not time_tag:
        #     time_tag = 'Unregistered'
        # return time_tag.text.strip()

    @property
    def party(self):
        party = self._soup.find('strong', {'class': 'title'}).text.strip().split(' ', 1)[0]
        return party

    # test URLS
    # http://www.armslist.com/posts/5577404/montgomery-alabama-handguns-for-sale-trade--ruger-44-magnum-7-5--super-blackhawk
    # http://www.armslist.com/posts/5534229/jacksonville-florida-rifles-for-sale--new-sig-sauer-mcx-5-56-rifle
    # http://www.armslist.com/posts/5577694/south-west-florida-handguns-for-sale--ar-pistol
