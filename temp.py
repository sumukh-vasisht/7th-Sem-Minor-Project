from credentials import twitter_credentials
from random import randint, seed
import random
import pandas as pd
import numpy as np
import json

CONSUMER_KEY = twitter_credentials.CONSUMER_KEY
CONSUMER_SECRET = twitter_credentials.CONSUMER_SECRET
OAUTH_TOKEN = twitter_credentials.ACCESS_TOKEN
OAUTH_TOKEN_SECRET = twitter_credentials.ACCESS_TOKEN_SECRET

value = randint(4000, 6500)
# print(value)

df = pd.read_csv('data/tweets_dataset.csv')
df = df.sample(20)
df = df.replace('@MumbaiPolice', '@PMOIndia', regex=True)
df['tweet'] = df['tweet'].str.replace('mumbai', '')
# print(df)

statesFile = open('data/states.json')
statesFileStr = statesFile.read()
statesData = json.loads(statesFileStr)
# print(statesData)
states = []
for key in statesData.keys():
    states.append(key)

print(states)

for index, row in df.iterrows():
    # print(row['tweet'])
    if('mumbai' in row['tweet'] or 'Mumbai' in row['tweet']):
        df.set_value(index, 'location', 'MH')
    else:
        df.set_value(index, 'location', random.choice(states))

count = df.query('complaint == 1').complaint.count()
print(count)



