import re
import gensim

########## Modular Functions ##########
def cleaning_text(text):
    clean_str = text.lower() # lowercase
    clean_str = re.sub(r"(?:\@|#|https?\://)\S+", " ", clean_str) # eliminate username, url, hashtags
    clean_str = re.sub(r'&amp;', '', clean_str) # remove &amp; as it equals &
    clean_str = re.sub(r'[^\w\s]',' ', clean_str) # remove punctuation
    clean_str = re.sub(r'[0-9]', '', clean_str) # remove number
    clean_str = re.sub(r'[\s\n\t\r]+', ' ', clean_str) # remove extra space
    clean_str = clean_str.strip() # trim
    return clean_str

def remove_stopwords(text, stopwords):
  clean_tokens = [w for w in text.split(" ") if (w not in stopwords) and (w != "")]
  clean_text = " ".join(clean_tokens)
  return clean_text

def stem_token(text, stemmer):
  stemmed_token = [stemmer.stem(w) for w in text.split(" ") if (w != "")]
  return " ".join(stemmed_token)

def tokenize_text(texts, tokenizer):
  tokenized_train = tokenizer.texts_to_sequences(texts)
  padded_tokens = sequence.pad_sequences(tokenized_train, maxlen=maxlen)
  return padded_tokens
