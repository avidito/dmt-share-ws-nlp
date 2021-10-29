import os
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

from google.cloud import storage
storage_client = storage.Client()
bucket = storage_client.get_bucket("dmt_share_leorio")

# Vocabulary
vocab_str = bucket.get_blob('api_metadata/vocabulary.txt').download_as_text()
vocab = [word.strip() for word in vocab_str.split("\n")]
vocab_size = len(vocab)

# Word Tokens
word_tokens_str = bucket.get_blob('api_metadata/word_tokens.txt').download_as_text()
word_tokens = [
    [
        word.strip()
        for word in word_token.strip("[]").split(",")
    ]
    for word_token in word_tokens_str.replace("'", "").split("\n")
]

# Initialize Word Tokens
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(word_tokens)

# Initialize Stemmer
stem = StemmerFactory()
stemmer = stem.create_stemmer()

model = None

def classify_title(title):
    global model
    if (model is None):
        model_path = os.path.join("/tmp", "model.h5")
        bucket.get_blob('api_metadata/model/classifier.h5').download_to_filename(model_path)
        model = tf.keras.models.load_model(model_path)

    maxlen = 19
    category = ["entertainment", "lifestyle", "sport", "technology"]

    clean_title = cleaning_text(title)
    stemmed_title = stem_token(clean_title, stemmer)
    padded_token = pad_sequences(tokenizer.texts_to_sequences([stemmed_title]), maxlen=maxlen)
    proba = model.predict(padded_token)

    result = category[np.argmax(proba[0])]
    ctg_proba = {
        ctg: p for ctg, p in zip(category, proba[0].tolist())
    }
    return (result, ctg_proba)

# Preprocessing
def cleaning_text(text):
    clean_str = text.lower() # lowercase
    clean_str = re.sub(r"(?:\@|#|https?\://)\S+", " ", clean_str) # eliminate username, url, hashtags
    clean_str = re.sub(r'&amp;', '', clean_str) # remove &amp; as it equals &
    clean_str = re.sub(r'[^\w\s]',' ', clean_str) # remove punctuation
    clean_str = re.sub(r'[0-9]', '', clean_str) # remove number
    clean_str = re.sub(r'[\s\n\t\r]+', ' ', clean_str) # remove extra space
    clean_str = clean_str.strip() # trim

    return clean_str

def stem_token(text, stemmer):
     stemmed_token = [stemmer.stem(w) for w in text.split(" ") if (w != "")]
     return " ".join(stemmed_token)
