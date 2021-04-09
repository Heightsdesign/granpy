from src.cleaner import Cleaner

# - Cleaner :

    # - Retrieve question attribute from Cleaner object

def test_get_question():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.question == "Granpy quelle est l'adresse de la Poste?"

    # - Turn question into all lowercases with lowercase method
    # - 'Poste' should be in all lowercase
    
def test_turn_lowercase():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.stopword() == ['poste']
    
    # - Turn question (string) in a world list with wordlist method

def test_turn_string_to_wordlist():
    testclnr2 = Cleaner("Granpy quelle est l'adresse de la Tour Eiffel?")
    assert testclnr2.stopword() == ['tour', 'eiffel']

    # - Clean worldlist from unwanted commun words with stopword method
    
def test_token():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.stopword() == ['poste']
    
    # - Retreive wordlist cleaned from stopword method

def test_get_token():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    print(testclnr1.stopword()[0])
