"""This file handles wikipedia requests and data"""

import wikipedia
import json

geocode_mock_data = ("OK", [48.85837009999999, 2.2944813])
geocode_mock_data2 = ("OK", [48.8975156, 2.3833993])
geocode_mock_data3 = ("OK", [43.94756599999999, 4.53496])


class WikiSearcher:
    # This handles the wikipedia requests and response
    # the data attribute passed is a geocoder object result

    def __init__(self, data):

        self.data = data
        self.lookup = []

    def __set_language(self):
        return wikipedia.set_lang("fr")

    def __set_lookup(self):

        self.__set_language()
        self.lookup = wikipedia.geosearch(
            self.data[1][0], self.data[1][1], results=5, radius=2000
        )
        return self.lookup

    def geolookup(self):

        self.__set_lookup()

        try:
            self.result = wikipedia.summary(self.lookup[0], sentences=2)

        except wikipedia.exceptions.PageError:
            self.result = wikipedia.summary(self.lookup[1], sentences=2)

        return self.result

    def get_url(self):

        self.__set_lookup()

        try:
            self.my_url = wikipedia.page(self.lookup[0]).url

        except wikipedia.exceptions.PageError:
            self.my_url = wikipedia.page(self.lookup[1]).url

        return self.my_url


wikisearch = WikiSearcher(geocode_mock_data2)
print(wikisearch.geolookup())
print(wikisearch.get_url())
