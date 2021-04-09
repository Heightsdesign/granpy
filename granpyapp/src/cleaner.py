
from nltk.corpus import stopwords
import spacy 

nlp = spacy.load("fr_core_news_sm")
stopWords = set(stopwords.words('french'))


class Cleaner:

    def __init__(self, question):

        self.question = question

    def __lowercase(self):

        self.question = self.question.lower()

        return self.question

    def __wordlist(self):

        wordlist = nlp(self.__lowercase())

        return [X.text for X in wordlist]

    def stopword(self):

        clean_words = []
        for token in self.__wordlist():
            if token not in stopWords:
                clean_words.append(token)

        return clean_words

    def concatenate(self):

        final_string = ""

        for word in self.stopword():
            final_string = final_string + word + "+"

        return final_string


testclnr = Cleaner("Granpy quelle est l'adresse de la Tour Eiffel?")






    