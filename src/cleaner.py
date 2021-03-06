"""This file contains the cleaner class uses the input given from
user and cleans the question, gives back token words"""

from src.stopwords import STOPWORDS
import spacy
nlp = spacy.load("fr_core_news_sm")


class Cleaner:
    def __init__(self, question):
        # initializes cleaner object takes question as attribute
        self.question = question
        self.final_string = ""

    def __lowercase(self):
        # turns the question in all lower cases

        self.question = self.question.lower()

        return self.question

    def __wordlist(self):
        # turns the string into a wordlist

        wordlist = nlp(self.__lowercase())

        return [X.text for X in wordlist]

    def __stopword(self):
        # uses a stopword list and deletes from list
        # unwanted words

        clean_words = []
        for token in self.__wordlist():
            if token not in STOPWORDS:
                clean_words.append(token)

        return clean_words

    def __concatenate(self):
        # concatenates the words selected by the stopword
        # method and adds a '+' between them to make request
        # in geocode.py

        for word in self.__stopword():
            self.final_string = self.final_string + word + "+"

    def make_final_string(self):
        # makes the final string to be used in geocode.py

        self.__concatenate()
        return self.final_string[:-1]


sut = Cleaner("Granpy quelle est l'adresse de la Poste?")
print(sut.make_final_string())
