#import sys
#sys.path.append('D:\Openclassrooms\P7\granpy\granpyapp')
from granpyapp.cleaner import Cleaner


# - Cleaner :
    # - Retrieve question attribute from Cleaner object
def get_question():
    testclnr1 = Cleaner("Granpy quelle est l'adresse de la Poste?")
    assert testclnr1.question == "Granpy quelle est l'adresse de la Poste?"
        
    # - Turn question into all lowercases with lowercase method
    # - Retreive question in lowercase
    # - Turn question (string) in a world list with wordlist method
    # - Retreive wordlist
    # - Clean worldlist from unwanted commun words with stopword method
    # - Retreive wordlist cleaned from stopword method