from nltk import TreebankWordTokenizer
from nltk import WordPunctTokenizer
from nltk import WhitespaceTokenizer


from textblob.base import BaseTokenizer



        
class NLTKTreebankWordTokenizer(BaseTokenizer):

    def tokenize(self, text):

        return TreebankWordTokenizer().tokenize(text)

class NLTKWordPunctTokenizer(BaseTokenizer):

    def tokenize(self, text):

        return WordPunctTokenizer().tokenize(text)


class NLTKWhitespaceTokenizer(BaseTokenizer):

    def tokenize(self, text):
        return WhitespaceTokenizer().tokenize(text)

        