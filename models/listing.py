from bs4 import BeautifulSoup

class Listing:
    def __init__(self, html):
        """Takes page elements and creates globacl class variables.

        The function recieves self and page html markup of a listing page then assigns
        it to global variables within the class. It also defines BeautifulSoup and
        makes two global variables for property use
        """
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
        self._characteristics = self._soup.find('ul', {'class': 'category'}).find_all('li')
        self._post_meta = self._soup.find('div', {'class': 'info-time'})

    @property
    def title(self):
        """Scrapes title.

        Finds first h1 on page, which is the title then makes it a string and strips extra space.
        """
        return self._soup.find('h1').string.strip()

    @property
    def price(self):
        """Scrapes price.

        The function searches for the 'price' span, converts to a string and strips it. If the price
        starts with anything but a dollar sign, returns price as the original string.
        """
        span_contents = self._soup.find('span', {'class': 'price'})
        price_string = span_contents.string.strip()
        if price_string.startswith('$'):
            junk, price = span_contents.string.strip().split('$ ')
            return price
        else:
            return price_string

    @property
    def img(self):
        """Scrapes first image url.

        Function searches for the all tagged gallery images, if any, then scrapes
        and returns the first image url.
        """
        image_tags = self._soup.find_all('img', {'class': 'gallery'}) # have to sort out repeats
        for image_tag in image_tags:
            image_url = image_tag['src']
            return image_url

    @property
    def full_location(self):
        """Scrapes full location string to breakdown.

        Function searches for the location icon class then takes a step back to the parent
        div. From there, the location is found by getting the second div and stripping it.
        """
        location_icon = self._soup.find('i', {'class': 'icon-location'})
        parent = location_icon.parent.parent
        location_div = parent.find_all('div')[1]
        return location_div.text.strip()

    @property
    def location(self):
        """Scrapes user-inputted location.

        Function uses the full location output and separate parts by comma.

        """
        parts = self.full_location.split(', ')
        return ', '.join(parts[0:-2])

    @property
    def city(self):
        """Scrapes city by armslist dropdown.

        Function uses the full location output and separate parts by comma.
        It then checks if US is input as the city and returns none or returns the city name.
        """
        parts = self.full_location.split(', ')
        if parts[-1] == 'United States':
            return None
        else:
            return parts[-2]

    @property
    def state(self):
        """Scrapes state by armslist dropdown.

        Function uses the full location output and separate parts by comma.
        It then checks if US is input as the state and returns city or returns the state name.
        """
        parts = self.full_location.split(', ')
        if parts[-1] == 'United States':
            return parts[-2]
        elif parts[-1] == 'South Florida':
            return 'Florida'
        else:
            return parts[-1]

    @property
    def description(self):
        """Scrapes description of gun.

        Function finds the div marked with the post content class, converts to text and strips.
        """
        desc = self._soup.find('div', {'class': 'postContent'})
        return desc.text.strip()

    @property
    def category(self):
        """Scrapes gun's category.

        Function uses the _characteristics variable to target the span with 'category' as content,
        then returns the value of next span associated
        """
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'category':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def manufacturer(self):
        """Scrapes gun's manufacturer.

        Function uses the _characteristics variable to target the span with 'manufacturer' as content,
        then returns the value of next span associated
        """
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'manufacturer':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def caliber(self):
        """Scrapes gun's caliber.

        Function uses the _characteristics variable to target the span with 'caliber' as content,
        then returns the value of next span associated
        """
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'caliber':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def action(self):
        """Scrapes gun's action.

        Function uses the _characteristics variable to target the span with 'action' as content,
        then returns the value of next span associated
        """
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'action':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def firearm_type(self):
        """Scrapes gun's firearm type.

        Function uses the _characteristics variable to target the span with 'firearm_type' as content,
        then returns the value of next span associated
        """
        for item in self._characteristics:
            key = item.find_all('span')[0].text.strip().lower()
            if key == 'firearm type':
                value = item.find_all('span')[1].text.strip()
                return value

    @property
    def listed_date(self):
        """Scrapes the listed date by span with 'date' class"""
        return self._post_meta.find('span', {'class': 'date'}).text.strip()

    @property
    def post_id(self):
        """Scrapes the post id by span with 'user-id' class"""
        return self._post_meta.find('span', {'class': 'user-id'}).text.strip().split(':  ')[1]

    @property
    def registered(self):
        """Returns a boolean for registration status

        Function finds the 'time' class and if there is a time tag associated,
        returns true, else returns false. Commented code can return registered or
        unregistered as strings vs. booleans
        """
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
        """Scrapes the associated party by strong tag with class 'title' then splits and strips excess"""
        party = self._soup.find('strong', {'class': 'title'}).text.strip().split(' ', 1)[0]
        return party
