"""This file contains the unit tests of the wiki file"""
import wikipedia
from wikipedia.wikipedia import WikipediaPage
from src.wiki import WikiSearcher
from unittest.mock import Mock, MagicMock
import pytest


def test_wiki_geolookup(monkeypatch):

    token = ("OK", [48.8975156, 2.3833993])
    sut = WikiSearcher(token)

    class MockResponseGeosearch(object):
        def geosearch():
            georesponse = [
                "Quai de la Gironde",
                "Parc du Pont de Flandre",
                "Square du Quai-de-la-Gironde",
                "Avenue Corentin-Cariou",
                "Porte de la Villette (métro de Paris)",
            ]
            return georesponse

        def summary():

            sumresponse = (
                "Le quai de la Gironde est un quai situé"
                " le long du canal Saint-Denis, "
                "à Paris, dans le 19e arrondissement."
                "== Situation et accès =="
                "Il fait face au quai de la Charente, "
                "commence au quai de l'Oise"
                " et se termine avenue Corentin-Cariou."
            )
            return sumresponse

        def results(self):

            result_wiki_sentence = (
                "Le quai de la Gironde est un quai situé"
                " le long du canal Saint-Denis, "
                "à Paris, dans le 19e arrondissement."
                "== Situation et accès =="
                "Il fait face au quai de la Charente, "
                "commence au quai de l'Oise"
                " et se termine avenue Corentin-Cariou."
            )
            return result_wiki_sentence

    def mock_get(*url, **args):
        return MockResponseGeosearch().results()

    monkeypatch.setattr(wikipedia, "geosearch", mock_get)
    monkeypatch.setattr(wikipedia, "summary", mock_get)

    assert (
        sut.geolookup() == "Le quai de la Gironde est un quai situé"
        " le long du canal Saint-Denis, "
        "à Paris, dans le 19e arrondissement."
        "== Situation et accès =="
        "Il fait face au quai de la Charente, "
        "commence au quai de l'Oise"
        " et se termine avenue Corentin-Cariou."
    )


def test_wiki_get_url(monkeypatch):

    token = ("OK", [48.8975156, 2.3833993])
    sut = WikiSearcher(token)

    class MockResponseUrl(object):
        def geosearch():

            georesponse = [
                "Quai de la Gironde",
                "Parc du Pont de Flandre",
                "Square du Quai-de-la-Gironde",
                "Avenue Corentin-Cariou",
                "Porte de la Villette (métro de Paris)",
            ]
            return georesponse

        class WikipediaPage(self):
            url = {"https://fr.wikipedia.org/wiki/Quai_de_la_Gironde"}

        def page():
            return WikipediaPage

        def results(self):

            result_wiki_url = "https://fr.wikipedia.org/wiki/Quai_de_la_Gironde"
            return result_wiki_url

    def mock_get(*url, **kwargs):
        return MockResponseUrl().results()

    monkeypatch.setattr(wikipedia, "geosearch", mock_get)
    monkeypatch.setattr(wikipedia, "page", mock_get)

    assert sut.get_url() == "https://fr.wikipedia.org/wiki/Quai_de_la_Gironde"
