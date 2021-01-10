import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from credentials import twitter_credentials
import json
import random
from random import randint, seed
from realtime import code

app = Flask(__name__)

CONSUMER_KEY = twitter_credentials.CONSUMER_KEY
CONSUMER_SECRET = twitter_credentials.CONSUMER_SECRET
OAUTH_TOKEN = twitter_credentials.ACCESS_TOKEN
OAUTH_TOKEN_SECRET = twitter_credentials.ACCESS_TOKEN_SECRET

categoriesData = {
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

data = {'KA':27, 'TN':15, 'AP':32,  
        'MH':35, 'GJ':47, 'AS': 12,
        'KL':41, 'MP':22, 'UP': 11,
        'ArP':27, 'DL':15, 'GA':32,  
        'RJ':35, 'PJ':47, 'UK': 12,
        'JK':41, 'HP':22, 'HR': 11} 
categories = list(data.keys()) 
number = list(data.values()) 
fig = plt.figure(figsize = (12, 5)) 
plt.bar(categories, number, color ='blue',  width = 0.4)   
plt.xlabel("States") 
plt.ylabel("No. of complaints") 
plt.title("States vs. number of complaints")
fig.savefig('static/images/plot3.png')
plt.figure()

def generateCNCPie(df):
    plt.figure()
    total = df['tweet'].count()
    complaints = getNumberOfComplaints(df)
    nonComplaints = total-complaints
    y = np.array([complaints, nonComplaints], dtype=object)
    mylabels = ["Complaints", "Non-Complaints"]
    explode = [0.1,0]
    plt.pie(y, labels = mylabels, explode = explode, autopct='%.1f%%')
    plt.title("Complaints vs. Non-Complaints")
    plt.savefig('static/images/plot1.png') 
    plt.figure()

def generatePercentageGraph(df):
    plt.figure()

    counts = df['category'].value_counts().rename_axis('unique_values').reset_index(name='counts')

    countList = counts['counts'].tolist()
    countList.pop(0)

    categoriesList = counts['unique_values'].tolist()
    categoriesList.pop(0)

    categories = []
    for i in categoriesList:
        if(i==18):
            index = categoriesList.index(18)
            countList.pop(index)
        else:
            categories.append(categoriesData[str(i)])

    y = np.array(countList, dtype=object)
    plt.pie(y, labels = categories)
    plt.title("Categories of Complaints")
    plt.savefig('static/images/plot2.png') 
    plt.figure()

def generateComplaintsBar(df):
    plt.figure()

    counts = df['category'].value_counts().rename_axis('unique_values').reset_index(name='counts')

    countList = counts['counts'].tolist()
    countList.pop(0)

    categoriesList = counts['unique_values'].tolist()
    categoriesList.pop(0)

    categories = []
    for i in categoriesList:
        if(i==18):
            index = categoriesList.index(18)
            countList.pop(index)
        else:
            categories.append(categoriesData[str(i)])

    y = np.array(countList, dtype=object)

    fig = plt.figure(figsize = (12, 10)) 
    plt.bar(categories, countList, color ='blue',  width = 0.4)
    plt.xticks(rotation='vertical')   
    plt.xlabel("Category") 
    plt.ylabel("No. of complaints") 
    plt.title("Categories vs. number of complaints")
    fig.savefig('static/images/plot3.png')

    plt.figure()

def generateLocationBar(df):
    plt.figure()

    df = df[df['complaint']==1]

    counts = df['location'].value_counts().rename_axis('unique_values').reset_index(name='counts')

    countList = counts['counts'].tolist()
    countList.pop(0)

    locations = counts['unique_values'].tolist()
    locations.pop(0)

    y = np.array(countList, dtype=object)

    fig = plt.figure(figsize = (12, 10)) 
    plt.bar(locations, countList, color ='blue',  width = 0.4)
    plt.xticks(rotation='vertical')   
    plt.xlabel("State") 
    plt.ylabel("No. of complaints") 
    plt.title("States vs. number of complaints")
    fig.savefig('static/images/plot4.png')

    plt.figure()

def getNumberOfComplaints(df):
    count = df.query('complaint == 1').complaint.count()
    return count

def generateGraphs():
    df = pd.read_csv('data/minedTweets.csv')
    generateCNCPie(df)
    generatePercentageGraph(df)
    generateComplaintsBar(df)
    generateLocationBar(df)
    return

def getStatesList():
    statesFile = open('data/states.json')
    statesFileStr = statesFile.read()
    statesData = json.loads(statesFileStr)
    states = []
    for key in statesData.keys():
        states.append(key)
    return states

@app.route('/')
def index():
    states = getStatesList()
    df = code.readData()
    numberOfTweets = df.shape[0]
    numberOfComplaints = getNumberOfComplaints(df)
    tweetText = df['tweet'].tolist()
    code.applyModel(df)
    generateGraphs()
    return render_template('index.html', tweets = numberOfTweets, complaints = numberOfComplaints, tweetText = tweetText)

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/tweetDetails/<i>')
def tweetDetails(i):
    details = code.getTweetDetails(int(i))
    tweet = details['tweet']
    date = details['date']
    complaint = details['complaint']
    if(complaint == 1):
        complaint = 'YES'
    else:
        complaint = 'NO'
    category = details['category']
    category = code.getCategory(str(category))
    location = details['location']
    likes = details['likes']
    retweets = details['retweets']
    return render_template('tweetDetails.html', tweet=tweet, length=len(tweet), date=date, complaint=complaint, category=category, location=location, likes=likes, retweets=retweets)

if __name__ == '__main__':
    app.run(debug=True)