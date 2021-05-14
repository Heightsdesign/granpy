""" This file tests the geocode file"""
import pytest
from src.geocode import Geocoder
import requests


""" - Geocoder """
""" Mocks the api resquest test if data is corresponding to the response """

val1 = {
    "results": [
        {"geometry": {"location": {"lat": 48.85837009999999, "lng": 2.2944813}}}
    ]
}

val2 = {"results": [], "status": "ZERO_RESULTS"}


@pytest.mark.parametrize(
    "input_value, expected",
    [(val1, ("OK", [48.85837009999999, 2.2944813])), (val2, ("NOK", []))],
)
def test_http_return(monkeypatch, input_value, expected):

    token = "tour+eiffel"
    sut = Geocoder(token)

    class MockResponse(object):
        def __init__(self):

            self.status_code = 200

        def json(self):

            response = input_value

            return response

    def mock_get(*url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert sut.get_location() == expected

    """Retrieve token from geocoder object"""


def test_get_token():

    token = "tour+eiffel"
    sut = Geocoder(token)
    assert sut.token == "tour+eiffel"

    # faire mock simuler le get , return lat et lng. monkey patch
