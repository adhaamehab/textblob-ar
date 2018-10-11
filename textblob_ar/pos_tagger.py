from nltk import StanfordPOSTagger
from textblob.taggers import BaseTagger
from pprint import pprint


class StanfordPartOfSpeechTagger(BaseTagger):
    """An interface for stanford arabic pos"""

    def __init__(self):
        modelPath = 'textblob_ar/data/arabic.tagger'
        modelJar = 'textblob_ar/data/model.jar'
        self._tagger = StanfordPOSTagger(modelPath, modelJar)

    def tag(self, text, tokenize=True):
        """Return a list of tuples of the form (word, tag)
        for a given set of text or BaseBlob instance.
        """

        if tokenize:
            tokens = text.tokens
        else:
            tokens = text
        tags = self._tagger.tag(tokens=tokens)
        result = []
        for tag in tags:
            if tag[0]:
                result.append(tuple(tag[1].split('/')))
            else:
                result.append(tag)
        return [i for i in result if len(i) == 2]
