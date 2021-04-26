"""This file contains the compiler class used to
compile the data fetched and formatted into the
cleaner.py, geocode.py and wiki.py files"""

from cleaner import Cleaner
from geocode import Geocoder
from wiki import WikiSearcher


class Compiler:

    def __init__(self, questn):

        self.questn = questn
        self.token = ""
        self.location = []

    def compile(self):

        self.token = Cleaner(self.questn).make_final_string()
        self.location = Geocoder(self.token).get_location()
        self.wikiresult = WikiSearcher(self.location).geolookup()

        self.finalData = {
            'status' : self.location[0],
            'lat': self.location[1][0],
            'long': self.location[1][1],
            'wikiresult' : self.wikiresult
        }

        return self.finalData


#generic_compiler = Compiler("Granpy quelle est l'adresse de la Tour Eiffel?")
#print(generic_compiler.compile()['lat'])