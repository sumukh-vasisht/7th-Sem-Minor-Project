from credentials import twitter_credentials
from random import randint, seed
import random
import pandas as pd
import numpy as np
import json
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

CONSUMER_KEY = twitter_credentials.CONSUMER_KEY
CONSUMER_SECRET = twitter_credentials.CONSUMER_SECRET
OAUTH_TOKEN = twitter_credentials.ACCESS_TOKEN
OAUTH_TOKEN_SECRET = twitter_credentials.ACCESS_TOKEN_SECRET

def applyModel(df):
    return

def readData():
    value = randint(4000, 6500)

    df = pd.read_csv('data/tweets_dataset.csv')
    df = df.sample(value)
    df = df.replace('@MumbaiPolice', '@PMOIndia', regex=True)
    df['tweet'] = df['tweet'].str.replace('mumbai', '')

    statesFile = open('data/states.json')
    statesFileStr = statesFile.read()
    statesData = json.loads(statesFileStr)
    states = []
    for key in statesData.keys():
        states.append(key)

    for index, row in df.iterrows():
        try:
            if('mumbai' in row['tweet'] or 'Mumbai' in row['tweet']):
                df.set_value(index, 'location', 'MH')
            else:
                df.set_value(index, 'location', random.choice(states))
        except:
            pass

    df['date'] = datetime.today().strftime('%Y-%m-%d')

    df.to_csv('data/minedTweets.csv')

    return df

def getTweetDetails(i):
    df = pd.read_csv('data/minedTweets.csv')
    details = df.iloc[i]
    details['likes'] = randint(0,250)
    details['retweets'] = randint(0, details['likes'])
    return details

def getCategory(id):
    categories = {
        '0': 'Not a complaint',
        '1': 'Trains',
        '2': 'Traffic',
        '3': 'Potholes',
        '4': 'Transport',
        '5': 'Illegal Parking',
        '6': 'Illegal Banners',
        '7': 'Noise',
        '8': 'Violence',
        '9': 'Frauds',
        '10': 'Harrassment',
        '11': 'Robbery',
        '12': 'Garbage',
        '13': 'High electricity bills',
        '14': 'Drinage and Water supply',
        '15': 'Missing Persons',
        '16': 'Electricity',
        '17': 'Gas'
    }
    return categories[id]
