# plotting graph here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

# test = pd.read_csv('test.csv', names=['A', 'B', 'C', 'D'])
# fig = test.plot.line().get_figure()
# fig.savefig('static/images/plot1.png')

# categories = ['Complaints', 'Non-Complaints']
# number = [250, 367]
# index = np.arange(len(categories))
# plt.bar(index, number)
# plt.xlabel('Categories', fontsize=5)
# plt.ylabel('No of Tweets', fontsize=5)
# plt.xticks(index, categories, fontsize=5, rotation=30)
# plt.title('Number of complaints and non-complaints')
# plt.savefig('static/images/plot1.png')

# c = ['Electricity', 'Traffic', 'Drinage', 'Water Problems', 'Pollution']
# n = [23,17,35,29,12]
# i = np.arange(len(c))
# plt.bar(i, n)
# plt.xlabel('Categories', fontsize=5)
# plt.ylabel('No of Complaints', fontsize=5)
# plt.xticks(i, c, fontsize=5, rotation=30)
# plt.title('Categories vs. Number of Complaints')
# plt.savefig('static/images/plot2.png')

y = np.array([350, 225])
mylabels = ["Complaints", "Non-Complaints"]
plt.pie(y, labels = mylabels, autopct='%.2f')
plt.title("Complaints vs. Non-Complaints")
# plt.legend()
plt.savefig('static/images/plot1.png') 

plt.figure()

y1 = np.array([20,15, 30, 35])
label = ["Traffic", "Electricity", "Pollution", 'Drinage']
plt.pie(y1, labels = label, autopct='%.2f')
plt.title("Percentage of different complaints")
# plt.legend()
plt.savefig('static/images/plot4.png') 


data = {'Traffic':20, 'Electricity':15, 'Pollution':30,  
        'Drinage':35} 
categories = list(data.keys()) 
number = list(data.values()) 
fig = plt.figure(figsize = (12, 5)) 
plt.bar(categories, number, color ='blue',  width = 0.4)   
plt.xlabel("Categories") 
plt.ylabel("No. of complaints") 
plt.title("Categories vs. number of complaints")
fig.savefig('static/images/plot2.png')

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

if __name__ == '__main__':
    app.run(debug=True)