"""This file contains the unit tests of the wiki file"""
import wikipedia
from src.wiki import WikiSearcher

def test_wiki_return(monkeypatch):

    token = ('OK', [48.8975156, 2.3833993])
    sut = WikiSearcher(token)

    class MockResponse(object):

        def geosearch():

            georesponse = [
                'Quai de la Gironde',
                'Parc du Pont de Flandre',
                'Square du Quai-de-la-Gironde',
                'Avenue Corentin-Cariou',
                'Porte de la Villette (métro de Paris)'
                ]

            return georesponse

        def summary():

            sumresponse = "Le quai de la Gironde est un quai situé" \
                        " le long du canal Saint-Denis, " \
                        "à Paris, dans le 19e arrondissement." \
                        "== Situation et accès ==" \
                        "Il fait face au quai de la Charente, " \
                        "commence au quai de l'Oise" \
                        " et se termine avenue Corentin-Cariou."

            return sumresponse

    def mock_get(*url, **args):
        return MockResponse()
    
    monkeypatch.setattr(wikipedia, 'geosearch', 'summary', mock_get)
    assert sut.geolookup() == "Le quai de la Gironde est un quai situé" \
                                " le long du canal Saint-Denis, " \
                                "à Paris, dans le 19e arrondissement." \
                                "== Situation et accès ==" \
                                "Il fait face au quai de la Charente, " \
                                "commence au quai de l'Oise" \
                                " et se termine avenue Corentin-Cariou."


