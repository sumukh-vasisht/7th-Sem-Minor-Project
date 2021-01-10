import pandas as pd
import json

df = pd.read_csv('data/minedTweets.csv')

df = df[df['complaint']==1]

# print(df)

counts = df['location'].value_counts().rename_axis('unique_values').reset_index(name='counts')
# print(counts)

countList = counts['counts'].tolist()
countList.pop(0)
# print(countList)

locations = counts['unique_values'].tolist()
locations.pop(0)
# print(locations)

# categoriesData = {
#         '0': 'Not a complaint',
#         '1': 'Trains',
#         '2': 'Traffic',
#         '3': 'Potholes',
#         '4': 'Transport',
#         '5': 'Illegal Parking',
#         '6': 'Illegal Banners',
#         '7': 'Noise',
#         '8': 'Violence',
#         '9': 'Frauds',
#         '10': 'Harrassment',
#         '11': 'Robbery',
#         '12': 'Garbage',
#         '13': 'High electricity bills',
#         '14': 'Drinage and Water supply',
#         '15': 'Missing Persons',
#         '16': 'Electricity',
#         '17': 'Gas'
#     }

# categories = []
# for i in categoriesList:
#     if(i==18):
#         index = categoriesList.index(18)
#         countList.pop(index)
#     else:
#         categories.append(categoriesData[str(i)])

# print(countList)
# print(categories)

# print(len(countList))
# print(len(categories))

# if(len(countList)!=17):
#     rem = 17-len(countList)
#     for i in range(rem):
#         countList.append(0)

# categories = ['Trains','Traffic','Potholes','Transport','Illegal Parking','Illegal Banners',
#         'Noise','Violence','Frauds','Harrassment','Robbery','Garbage','High electricity bills',
#         'Drinage and Water supply','Missing Persons','Electricity','Gas']

# data = {}

# for key in categories:
#     for value in countList:
#         data[key] = value

# print(data)
