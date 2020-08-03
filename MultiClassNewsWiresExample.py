import tensorflow as tf
from tensorflow import keras
from keras.datasets import reuters
from keras import layers
from keras import models

import numpy as np
import matplotlib.pyplot as plt

#Loading Reuters dataset
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000) #restricts data to 10000 most frequent words in dataset

#Decoding newswires to text
#Currently each news wire is a list of integers, corresponding to word indicies of a dictionary
word_index =  reuters.get_word_index()
reverse_word_index = dict([ (value, key) for (key, value) in word_index.items() ])
decoded_newswire = ' '.join( [ reverse_word_index.get(i - 3, '?') for i in train_data[0] ] )

#label associated with an example is an integer between 0 and 45; corresponding to a topic index\

#Encoding data
def vectorise_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

x_train = vectorise_sequences(train_data)
x_test = vectorise_sequences(test_data)


#Encoding labels using catergorical encoding/one-hot encoding
def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    # print("results init: ", results)
    for i, labels in enumerate(labels):
        results[i, labels] = 1
    # print("results: ", results)
    # print("length of results: ", len(results))
    # print("length of element in results: ", len(results[0]))
    return results

one_hot_train_labels = to_one_hot(train_labels) #a matrix of 8982 lists of zeros of length 48 (48 different label/topic categories) 
#(corresponding to the labels of 8982 news wires) with a 1 at the index in range [0, 47] corresponding to the one of the 48 topics describing the news wire

one_hot_test_labels = to_one_hot(test_labels)

# fake_y_test = np.array(test_labels) #could've encoded the labels as such; each entry in the array representing the label for each of the test data point
#the integers at each index are in range [0, 47] corresponding to one of the 48 label categories
#we'd have to change our loss function to 'sparse_categorical_crossentropy'

# print("arr: ", fake_y_test, " len: ", len(fake_y_test))
#a matrix of 2246 lists of zeros of length 48 (48 different label/topic categories) 
#(corresponding to the labels of 2246 news wires) with a 1 at the index in range [0, 47] corresponding to the one of the 48 topics describing the news wire

# we could've done the above with the built in keras "to_categorical" function
# from keras.utils.np_utils import to_categorical
# one_hot_train_labels = to_categorical(train_labels)
# one_hot_test_labels = to_categorical(test_labels)

#Building network
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,))) #using 64 units b/c we want to prevent information bottlenecks
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax')) #46 for the number of categories in output and softmax activation to give us a probability distribution 
#in range [0,1] for each of the 46 categories, namely, a list of 46 numbers [0,1] as each output dictating the probability each input is of a category, 
#0 being least probable, and 1 being highly plausible

#Compilation
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy']) #notice that unlike binary classification, we're using
#categorical_crossentropy as the loss function here

#Setting aside a validation set x_val and y_val of 1000 samples form training data
x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]

history = model.fit(partial_x_train, partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val))

#Plotting training and validation loss
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()