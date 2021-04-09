"""This file contacts the google API and retrieves necessary data
i.e location"""

import requests
import json
from cleaner import testclnr as tcl


class Geocoder():
    #makes a request to google api geocoding to return location 
    #of users interest takes token (Cleaner object) as arg

    def __init__(self, token):

        self.token = token
        self.api_key = 'AIzaSyCIxX5J017B85kHREmxUrG6blTmkeJFV2c'
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    def __form_req(self):
        #formats a string used for the request

        req = self.url + self.token.concatenate() + '&key=' + self.api_key
        return req

    def __make_req(self):
        #makes the request, gets the data back in json format
        try:

            r = requests.get(self.__form_req())
        
        except ValueError:
            print('No information available for this request')

        return r.json()

    def save(self):
        #saves the request in json file called geocode.json

        with open('geocode.json', 'w') as f:
            data = self.__make_req()
            json.dump(data, f, indent=4)

    def get_location(self):
        #gets lattitude and longitude from json file
        #zips lattitude and longitude in a list

        with open('geocode.json', 'r') as f:
            data = json.load(f)
            lattitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            location = [lattitude, longitude]
        return location


geocoder = Geocoder(tcl)
geocoder.save()
print(geocoder.get_location())


#r = requests.get(url + '{}' + 'CAkey=' + '{}').format(token, api_key)

