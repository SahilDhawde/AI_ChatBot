import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lem=WordNetLemmatizer()

intents=json.loads(open('D:\Project\ChatBot\intents.json').read())

words=[]
classes=[]
documents=[]
ignore_lettres=[]

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordlist= nltk.word_tokenize(pattern)
        words.extend(wordlist)
        documents.append((wordlist,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#print(documents)

words = [lem.lemmatize(word) for word in words if word not in ignore_lettres]
words = sorted(set(words))

#print(words)

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl','wb'))
pickle.dump(classes, open('classes.pkl','wb'))

training = []

output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns= document[0]
    word_patterns=[lem.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])]=1
    training.append([bag,output_row])

random.shuffle(training)
training=np.array(training)

#print(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128,input_shape=(len(train_x[0]),), activation= 'relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation= 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]),activation= 'softmax'))

sgd = SGD(learning_rate=0.01,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

hist= model.fit(np.array(train_x), np.array(train_y),epochs=200,batch_size=5,verbose=1)
model.save('D:\Project\ChatBot\chatbot_model.h5',hist)
print('Done')







