"""This file handles wikipedia requests and data"""

import wikipedia

geocode_mock_data = ("OK", [48.85837009999999, 2.2944813])
geocode_mock_data2 = ('OK', [48.8975156, 2.3833993])

class WikiSearcher:
    # This handles the wikipedia requests and response
    # the data attribute passed is a geocoder object result

    def __init__(self, data):

        self.data = data
        self.lookup = []

    def __set_language(self):
        return wikipedia.set_lang("fr")

    def geolookup(self):
        
        self.__set_language()
        self.lookup = wikipedia.geosearch(self.data[1][0], self.data[1][1], results=5, radius=1000)
        result = wikipedia.summary(self.lookup[0], sentences=2)
        return result

#wikisearch = WikiSearcher(geocode_mock_data2)
#print(wikisearch.geolookup())
