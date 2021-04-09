""" This file tests the google_api file"""

from src.geocode import Geocoder as geo
import src.cleaner as cl
# - Geocoder

    # Retrieve token from geocoder object

def test_get_token():
    tstgeo = geo(cl.testclnr)
    assert tstgeo.token == [48.85837009999999, 2.2944813]

