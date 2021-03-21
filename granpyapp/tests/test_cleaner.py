import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from cleaner import Cleaner


# - Cleaner :

    # - Retrieve question attribute from Cleaner object

def test_get_question():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.question == "Granpy quelle est l'adresse de la Poste?"
        
    # - Turn question into all lowercases with lowercase method
def test_turn_lowercase():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.lowercase() == "granpy quelle est l'adresse de la poste?"

    # - Retreive question in lowercase
def test_get_question_in_lowercase():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    print(testclnr1.lowercase())

    # - Turn question (string) in a world list with wordlist method
def test_turn_string_to_wordlist():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.wordlist() == ["granpy", "quelle", "est", "l'", "adresse", "de", "la", "poste", "?"]

    # - Retreive wordlist
def test_get_wordlist():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    print(testclnr1.wordlist())

    # - Clean worldlist from unwanted commun words with stopword method
def test_token():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.stopword() == ['poste']

    # - Retreive wordlist cleaned from stopword method

def test_get_token():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    print(testclnr1.stopword()[0])