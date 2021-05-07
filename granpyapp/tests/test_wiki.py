"""This file contains the unit tests of the wiki file"""
import wikipedia
from src.wiki import WikiSearcher
from unittest.mock import Mock, MagicMock

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

        def url():

            urlresponse = "https://fr.wikipedia.org/wiki/Quai_de_la_Gironde"
            return urlresponse

        
        def results(self):

            result_wiki_sentence = "Le quai de la Gironde est un quai situé" \
                                " le long du canal Saint-Denis, " \
                                "à Paris, dans le 19e arrondissement." \
                                "== Situation et accès ==" \
                                "Il fait face au quai de la Charente, " \
                                "commence au quai de l'Oise" \
                                " et se termine avenue Corentin-Cariou."

            return result_wiki_sentence


    def mock_get(*url, **args):
        return MockResponse().results()
    
    monkeypatch.setattr(wikipedia, 'geosearch', mock_get)
    monkeypatch.setattr(wikipedia, 'summary', mock_get)
    assert sut.geolookup() == "Le quai de la Gironde est un quai situé" \
                                " le long du canal Saint-Denis, " \
                                "à Paris, dans le 19e arrondissement." \
                                "== Situation et accès ==" \
                                "Il fait face au quai de la Charente, " \
                                "commence au quai de l'Oise" \
                                " et se termine avenue Corentin-Cariou."


