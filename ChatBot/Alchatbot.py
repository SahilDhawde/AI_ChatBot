import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow

from keras.models import load_model

model=load_model('D:\Project\ChatBot\chatbot_model.h5')

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lem=WordNetLemmatizer()

intents=json.loads(open('D:\Project\ChatBot\intents.json').read())

words=pickle.load( open('words.pkl','rb'))
classes=pickle.load( open('classes.pkl','rb'))

bot_name= "Chat Bot"


#print(classes)

def clean_up_sen(sentence):
    sen_words = nltk.word_tokenize(sentence)
    sen_words = [lem.lemmatize(word) for word in sen_words]
    return sen_words

def bag_of_words(sentence):
    sen_words = clean_up_sen(sentence)
    bag = [0] * len(words)
    for w in sen_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_Thres = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_Thres ]

    results.sort(key=lambda x: x[1], reverse=True)
    result_list=[]
    for r in results:
        result_list.append({'intents':classes[r[0]], 'probability': str(r[1])})
    return result_list

def get_response(intents_list,intents_json):
    tag = intents_list[0]['intents']
    list_of_int= intents_json['intents']
    for i in list_of_int:
        if i['tag']== tag:
            result = random.choice(i['responses'])
            break
    return result

print("GO, Bot is running!...")

def msgg(message):
#while True:
    #message=input("")
    ints=predict_class(message)
    res=get_response(ints,intents)
    return res




