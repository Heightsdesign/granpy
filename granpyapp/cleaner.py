

from nltk.corpus import stopwords
import spacy 

nlp = spacy.load("fr_core_news_sm")
stopWords = set(stopwords.words('french'))


class Cleaner:

    def __init__(self, question):

        self.question = question

    def lowercase(self):

        self.question = self.question.lower()

        return self.question

    def wordlist(self):

        wordlist = nlp(self.lowercase())

        return [X.text for X in wordlist]

    def stopword(self):

        clean_words = []
        for token in self.wordlist():
            if token not in stopWords:
                clean_words.append(token)

        return clean_words


testclnr = Cleaner("Granpy quelle est l'adresse de la poste?")
print(testclnr.stopword())





    