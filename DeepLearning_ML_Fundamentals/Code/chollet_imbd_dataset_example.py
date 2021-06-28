"""
author: William Darko (repurposed from original author Francois Chollet)
date: June, 2021
description: Two-class (binary) classification using IMDB dataset to classify movie review as positive or negative. The original code sample
is provided by Francois Chollet in his 'Deep Learning with Python' (1st Edition, Manning publisher)
"""


import numpy as np
import tensorflow as tf
from tensorflow import keras

from keras.datasets import imdb

# loading the IMBD dataset

(training_data, training_labels), (testing_data, testing_labels) = imdb.load_data(num_words=10000)
# num_words argument denotes taking the top 10000 most frequent words in the training_data
# training_data, and testing_data are list of reviews where each review is a list of word indices like [1, 14, 28, 99, 299, 87...] from a dictionary of words
# thus the first word in a review [1, 14, 28, 99, 299, 87...], the word at index 0 of the review, is the word at index 1 of the dictionary.
# training_labels and testing_labels are list of 1s and 0s classifying a word as positive, or negative, respectively

print(training_data[0])

# preparing the data

# one way is to pad the lists to the same length and turn them into integer tensors of shape (samples, word_indices) and use Embedding as the first layer
# other way is to 'One-hot' encode lists, meaning to turn them into vectors of 0s and 1s where 0 denotes no presense of that letter and 1 the opposite
# using One-hot encoding we create a list of length 10000 where there are 0s every where except for the indices which corresponding letters appear in the review sequence

def encode_sequences(sequences, dimesion=10000):
    results =  np.zeros((len(sequences),dimesion))
    for i, review in enumerate(sequences):
        results[i, review] = 1 # equivalent of iterating a through review with a second counter j, and doing results[i][j] = 1
    return results

x_train_data = encode_sequences(training_data)
x_test_data = encode_sequences(testing_data)

y_train_data = np.asarray()

