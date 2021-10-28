import os
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

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

model = None

def classify_title(title):
    global model
    if (model is None):
        model_path = os.path.join("/tmp", "model.h5")
        bucket.get_blob('api_metadata/model/classifier.h5').download_to_filename(model_path)
        model = tf.keras.models.load_model(model_path)

    maxlen = 19
    category = ["entertainment", "lifestyle", "sport", "technology"]

    padded_token = pad_sequences(tokenizer.texts_to_sequences([title]), maxlen=maxlen)
    proba = model.predict(padded_token)

    result = category[np.argmax(proba[0])]
    ctg_proba = {
        ctg: p for ctg, p in zip(category, proba[0])
    }
    return result, ctg_proba
