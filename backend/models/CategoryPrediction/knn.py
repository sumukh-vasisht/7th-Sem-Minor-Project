import io
import numpy as np
import pandas as pd
import csv
from collections import Counter
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score

np.random.seed(500)

dataset = pd.read_csv("../../data/preprocessed_dataset.csv", encoding='utf-8')

feature_col = ['preprocessed'] 
predicted = ['category'] 
X = dataset[feature_col].values
# print(X.shape)
y = dataset[predicted].values
# print(y.shape)

split_size=0.20
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=split_size,random_state=42)
Encoder = LabelEncoder()
y_train = Encoder.fit_transform(y_train.ravel())
y_test = Encoder.fit_transform(y_test.ravel())

Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(X.ravel().astype('U'))
Train_X_Tfidf = Tfidf_vect.transform(X_train.ravel().astype('U'))
Test_X_Tfidf = Tfidf_vect.transform(X_test.ravel().astype('U'))

def knn():
	knn = KNeighborsClassifier(n_neighbors=17)
	knn.fit(Train_X_Tfidf,y_train)
	y_pred=knn.predict(Test_X_Tfidf)
	print("KNeighborsClassifier Accuracy Score with columns(",feature_col, predicted,") -> ",accuracy_score(y_pred, y_test)*100)

knn()
