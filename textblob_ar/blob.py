import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from textblob.blob import BaseBlob, Word, WordList
from textblob.compat import unicode
from textblob.decorators import requires_nltk_corpus
from textblob_ar.sentiment import PatternAnalyzer
from textblob_ar.tokenizer import WordPunctTokenizer


class WordAR(Word):
    """Arabic Word representation and basic ops"""
    

    def translate(self, to='en'):
        """Translate the word from arabic to another language using Google's
        Translate API.
        :param to: string represents the language code for the target language. 
        """
        return Word.translate(from_lang='ar', to=to)
   
    def spellcheck(self):
        raise NotImplementedError 
    
    def correct(self):
        raise NotImplementedError
    

    @requires_nltk_corpus
    def singularize(self):
        """Return the singular version of the word as a Word."""
        raise NotImplementedError

    @requires_nltk_corpus
    def pluralize(self):
        '''Return the plural version of the word as a Word.'''
        raise NotImplementedError
    
    # todo 
    # word description
    # arabic diacritics


class WordlistAR(WordList):
    """Wordlist Data structure
    
    A list-like data structure to process words customized for arabic words. 
    """

    def count(self, strg,  *args, **kwargs):
        """Get the count of a word or phrase `s` within this WordList.
        Overrides textblob base wordlist.
        :param strg: The string to count.
        """
        return self._collection.count(strg, *args, **kwargs)

    def lemmatize(self):
        """Return the lemma of each word in this WordList."""
        
        return self.__class__([i.lemma() for i in self])


class TextBlob(BaseBlob):
    

    def __init__(self, text, tokenizer=None,
                 pos_tagger=None,
                 np_extractor=None,
                 analyzer=None,
                 parser=None,
                 classifier=None, clean_html=False):
        
        _tokenizer = tokenizer if tokenizer is not None else WordPunctTokenizer()
        _analyzer = analyzer if analyzer is not None else PatternAnalyzer()
        super().__init__(text=text, tokenizer=_tokenizer, analyzer=_analyzer, clean_html=clean_html)

    def stopwords(self):
        '''Return list of arabic stopwords'''
        return nltk.corpus.stopwords.words("arabic")

    