import re,string
import itertools
import io
import numpy as np
import pandas as pd
import csv
from collections import Counter
from symspellpy.symspellpy import SymSpell, Verbosity
from textblob import TextBlob
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import nltk
from stemming.porter2 import stem

np.random.seed(2018)

dico = {}

def setup_dictionary():
    dico1 = open('dicos/dico1.txt', 'rb')
    for word in dico1:
        word = word.decode('utf8')
        word = word.split()
        dico[word[1]] = word[3]
    dico1.close()
    dico2 = open('dicos/dico2.txt', 'rb')
    for word in dico2:
        word = word.decode('utf8')
        word = word.split()
        dico[word[0]] = word[1]
    dico2.close()
    dico3 = open('dicos/dico2.txt', 'rb')
    for word in dico3:
        word = word.decode('utf8')
        word = word.split()
        dico[word[0]] = word[1]
    dico3.close()

#To get correct spellings
def correct_spell(tweet):
    tweet = tweet.split()
    for word in tweet:
        if(word in dico.keys()):
            word = dico[word]
    tweet = ' '.join(tweet)
    return tweet

#To remove links in tweets
def remove_link(tweet):
    tweet = re.sub(r'http.?://[^\s]+[\s]?','', tweet)
    tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
    return tweet

def lemmatize_stemming(text):
    return stem(WordNetLemmatizer().lemmatize(text, pos='v'))

#To seperate the contractions and punctuations
def clean_dataset(tweet):
    tweet = remove_link(tweet)
    tweet = re.sub(r"i'm", "i am", tweet)
    tweet = re.sub(r"he's","he is",tweet)
    tweet = re.sub(r"she's","she is",tweet)
    tweet = re.sub(r"that's","that is",tweet)
    tweet = re.sub(r"what's","what is",tweet)
    tweet = re.sub(r"where's","where is",tweet)
    tweet = re.sub(r"\'ll","will",tweet)
    tweet = re.sub(r"\'re","are",tweet)
    tweet = re.sub(r"\'d","would",tweet)
    tweet = re.sub(r"won't","will not",tweet)
    tweet = re.sub(r"can't","can not",tweet)
    tweet = re.sub(r"[-()\";:<>{}+=?,]","",tweet)
    tweet = re.sub('\d+','', tweet)
    tweet = re.sub(r'[^\x00-\x7F]+','',tweet)

    punct=string.punctuation
    transtab=str.maketrans(punct,len(punct)*' ')

    tweet = correct_spell(tweet)

    return tweet.strip()

#To remove hashtags and mentions in a tweet
def remove_hashtag(tweet):
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'#\w+','', tweet)
    tweet = remove_link(tweet)
    tweet = clean_dataset(tweet)
    return(tweet.strip())

#To remove stopwords
def remove_stopwords(tweet):
    result = []
    for token in gensim.utils.simple_preprocess(tweet):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token)>3:
            result.append(lemmatize_stemming(token))
    result = ' '.join(str(x) for x in result)
    return str(result)

def preprocess(tweet):
    result = []
    for token in gensim.utils.simple_preprocess(tweet):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))

    result=" ".join(str(x) for x in result)
    return str(result)

def no_propernoun(tweet):
    tweet = list(tweet.split(' '))
    for i in tweet:
        if i not in dico.values():
            tweet.remove(i)
    tweet = ' '.join(str(x) for x in tweet)
    return str(tweet)

#To remove links in tweets
def get_processed_dataset():
    dataset = pd.read_csv('../data/tweets_dataset.csv', encoding="ISO-8859-1")
    final_dataset = pd.read_csv('../data/tweets_dataset.csv', encoding="ISO-8859-1")
    print('CLEANING DATASET')
    dataset['cleaned']=dataset['tweet'].astype(str).apply(clean_dataset)
    print('REMOVING HASHTAG')
    dataset['hashtag'] = dataset['cleaned'].astype(str).apply(remove_hashtag)
    print("REMOVING STOPWORDS")
    dataset['without_stopword']=dataset['hashtag'].astype(str).apply(remove_stopwords)
    print("LEMMATIZING")
    dataset['lemmatize'] = dataset['without_stopword'].astype(str).apply(preprocess)
    print("REMOVING PROPER NOUNS")
    dataset['without_propernoun'] = dataset['lemmatize'].astype(str).apply(no_propernoun)
    final_dataset['preprocessed'] = dataset['without_propernoun']
    final_dataset.to_csv('../data/preprocessed_dataset.csv', sep = ',', encoding = 'utf-8')
    # print(dataset)
    print('Saved file')

setup_dictionary()
get_processed_dataset()


