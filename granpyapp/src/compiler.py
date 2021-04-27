"""This file contains the compiler class used to
compile the data fetched and formatted into the
cleaner.py, geocode.py and wiki.py files"""

from cleaner import Cleaner
from geocode import Geocoder
from wiki import WikiSearcher
import random
from config import NOK_response_sentences as nok_res

class Compiler:

    def __init__(self, questn):

        self.questn = questn
        self.token = ""
        self.location = []

    def compile(self):

        self.token = Cleaner(self.questn).make_final_string()
        self.location = Geocoder(self.token).get_location()

        if self.location[0] == "OK":

            self.wikiresult = WikiSearcher(self.location).geolookup()
            self.wikiurl = WikiSearcher(self.location).get_url()

            self.finalData = {
                'status' : self.location[0],
                'lat': self.location[1][0],
                'long': self.location[1][1],
                'wikiresult' : self.wikiresult,
                'wikiurl': self.wikiurl
            }

        else:

            self.finalData = {
                'status' : self.location[0],
                'warningMessage' : random.choice(nok_res)
            }


        return self.finalData
