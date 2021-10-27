import os
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Tokenization
vocab_path = os.path.join(os.getcwd(), "application", "module", "classify", "model", "vocabulary.txt")
with open(vocab_path, "r", encoding="utf-8") as file:
    vocab = file.readlines()
vocab_size = len(vocab)

word_tokens_path = os.path.join(os.getcwd(), "application", "module", "classify", "model", "vocabulary.txt")
with open(word_tokens_path, "r", encoding="utf-8") as file:
    raw_word_tokens = file.readlines()
word_tokens = [
    [token.strip().replace("'", "").strip()
    for word_token in raw_word_tokens for token in word_token.strip().strip("[]").split(",")]
]

tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(word_tokens)

# Model
model_path = os.path.join(os.getcwd(), "application", "module", "classify", "model", "classifier.h5")
model = tf.keras.models.load_model(model_path)

def classify_title(title):
    maxlen = 19
    category = ["entertainment", "lifestyle", "sport", "technology"]

    padded_token = pad_sequences(tokenizer.texts_to_sequences([title]), maxlen=maxlen)
    proba = model.predict(padded_token)

    result = category[np.argmax(proba[0])]
    return result, proba[0].tolist()
