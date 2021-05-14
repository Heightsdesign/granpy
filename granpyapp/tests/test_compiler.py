import src.compiler as compiler
from compiler import cleaner
import random
from src.config import OK_response_sentences as ok_res


def test_compiler():

    token = "Granpy ou se trouve la Tour Eiffel ?"
    sut = compiler.Compiler(token)

    results = {
        "status": "OK",
        "lat": 48.85837009999999,
        "long": 2.2944813,
        "wikiresult": "La tour Eiffel  est une tour de fer"
        "puddlé de 324 mètres de hauteur (avec antennes) située à Paris,"
        "à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure"
        "de la Seine dans le 7e arrondissement."
        "Son adresse officielle est 5, avenue Anatole-France.",
        "wikiurl": "https://fr.wikipedia.org/wiki/Tour_Eiffel",
        "granpyMessage": random.choice(ok_res),
    }

    assert sut == results
