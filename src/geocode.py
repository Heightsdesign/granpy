"""This file contacts the google API and retrieves necessary data
i.e location"""

import requests
import os

class Geocoder:
    # makes a request to google api geocoding to return location
    # of users interest takes token (Cleaner object) as arg

    def __init__(self, token):

        self.token = token
        self.api_key = os.environ.get("GOOGLE_GEOCODING_API_KEY")
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address="
        self.status = ""
        self.location = []

    def __form_req(self):
        # formats a string used for the request

        req = self.url + self.token + "&key=" + self.api_key
        return req

    def __make_req(self):
        # makes the request, gets the data back in json format

        self.r = requests.get(self.__form_req())

        if self.r.status_code != 200:
            print("No response from server ! ")

        return self.r.json()

    def get_location(self):
        # gets the location, zips it in
        # tuple with status

        data = self.__make_req()

        try:
            if data["results"] == []:
                self.status = "NOK"

            else:

                self.status = "OK"
                # gets lattitude and longitude from json obj
                # zips lattitude and longitude in a list
                lattitude = data["results"][0]["geometry"]["location"]["lat"]
                longitude = data["results"][0]["geometry"]["location"]["lng"]
                self.location = [lattitude, longitude]

        except IndexError:
            self.status = "NOK"

        return self.status, self.location
