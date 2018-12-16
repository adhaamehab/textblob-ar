import numpy as np
import gensim
#from gensim.models.KeyedVectors import load_word2vec_format
from scipy import spatial

from textblob_ar.tokenizer import NLTKWordPunctTokenizer
from textblob_ar.utils import clean_str


class TextSimilarity:

    def __init__(self):
        try:
            self.model = gensim.models.KeyedVectors.load_word2vec_format('wiki.ar.vec')
            self.index2word_set = set(self.model.wv.index2word)
        except FileNotFoundError:
            raise FileNotFoundError
    def avg_feature_vector(self, sentence, num_features=300):
        words = NLTKWordPunctTokenizer().tokenize(clean_str(sentence))
        feature_vec = np.zeros((num_features, ), dtype='float32')
        n_words = 0
        for word in words:
            if word in self.index2word_set:
                n_words += 1
                feature_vec = np.add(feature_vec, self.model[word])
        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        return feature_vec

    def similarity(self, sentence1, sentence2):
        vec1, vec2 = self.avg_feature_vector(sentence1), self.avg_feature_vector(sentence2)
        return self.cosine_similarity(vec1, vec2)

    def cosine_similarity(self, vec1, vec2):
        return 1 - spatial.distance.cosine(vec1, vec2)