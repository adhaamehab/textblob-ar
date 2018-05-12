from __future__ import absolute_import
from textblob.base import BaseSentimentAnalyzer, CONTINUOUS
from textblob.translate import Translator
from textblob.sentiments import PatternAnalyzer as PA


class PatternAnalyzer(BaseSentimentAnalyzer):

    '''Sentiment analyzer that uses the same implementation as the
    pattern library. Returns results as a tuple of the form:
    ``(polarity, subjectivity)``
    '''

    kind = CONTINUOUS

    def analyze(self, text):
        """Return the sentiment as a tuple of the form:
        ``(polarity, subjectivity)``

        First the text is translated into english text
        using base translator from textblob then
        the sentiment is calculated by PatternAnalyzer
        """
        translated_text = Translator().translate(text, from_lang='ar')
        return PA().analyze(translated_text)

