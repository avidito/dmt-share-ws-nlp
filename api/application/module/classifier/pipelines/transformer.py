from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

########## Transformer ##########
class DataPreprocessing(BaseEstimator, TransformerMixin):
  def __init__(self, stopwords, stemmer):
    self.stopwords = stopwords
    self.stemmer = stemmer

  def fit(self, X, y = None):
    return self

  def transform(self, X, y = None):
    X_ = X.copy()
    X_clean_word = [cleaning_text(x) for x in X_ if (x != "")]
    X_clean_token = [remove_stopwords(x, self.stopwords) for x in X_clean_word if (x != "")]
    X_preprocessed = [stem_token(x, self.stemmer) for x in X_clean_token if (x != "")]
    return X_preprocessed

class FeatureEngineering(BaseEstimator, TransformerMixin):
  def __init__(self, tokenizer):
    self.tokenizer = tokenizer

  def fit(self, X, y = None):
    return self

  def transform(self, X, y = None):
    X_ = X.copy()
    X_padded = tokenize_text(X_, self.tokenizer)
    return X_padded
