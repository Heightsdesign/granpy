from src.cleaner import Cleaner

# - Cleaner :

""" Retrieve question attribute from Cleaner object """

def test_get_question():
    sut = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert sut.question == "Granpy quelle est l'adresse de la Poste?"

    """ Turn question into all lowercases with lowercase method
        'Poste' should be in all lowercase """
    
def test_turn_lowercase():
    sut = Cleaner("Granpy quelle est l'adresse de la POSTE?")
    assert sut.make_final_string() == "poste"
    
    """ Turn question (string) in a world list with wordlist method
    this method should seperate the words contained in the input string """

def test_turn_string_to_wordlist():
    sut = Cleaner("Granpy quelle est l'adresse de la Tour Eiffel?")
    assert sut.make_final_string() == "tour+eiffel"

    """ Clean worldlist from unwanted commun words with stopword method """
    
def test_token():
    sut = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert sut.make_final_string() == "poste"
    
    """ Takes words from wordlist and adds a + in between """

def test_concatenate():
    sut = Cleaner("Granpy quelle est l'adresse de la Tour Eiffel?")
    assert sut.make_final_string() == "tour+eiffel"

    """ Returns the final string """

def test_final_string():
    sut = Cleaner("Granpy quelle est l'adresse de la Tour Eiffel?")
    assert sut.make_final_string() == "tour+eiffel"