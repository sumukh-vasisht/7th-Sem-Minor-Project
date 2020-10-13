import io
import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

Encoder = LabelEncoder()

dataset = pd.read_csv("../data/preprocessed_dataset.csv", encoding='utf-8')

feature_column = ['preprocessed']
predicted = ['complaint']
X = dataset[feature_column].values
# print(X.shape)
y = dataset[predicted].values
# print(y.shape)

split_size = 0.20
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = split_size, random_state=42)

y_train = Encoder.fit_transform(y_train.ravel())
y_test = Encoder.fit_transform(y_test.ravel())

Tfidf_vector = TfidfVectorizer(max_features=5000)
Tfidf_vector.fit(X.ravel().astype('U'))
Train_X_Tfidf = Tfidf_vector.transform(X_train.ravel().astype('U'))
Test_X_Tfidf = Tfidf_vector.transform(X_test.ravel().astype('U'))

def nb():
    Naive = naive_bayes.MultinomialNB()
    Naive.fit(Train_X_Tfidf, y_train)
    predictions = Naive.predict(Test_X_Tfidf)
    print("Naive Bayes Accuracy Score with columns(",feature_column, predicted,") -> ",accuracy_score(predictions, y_test)*100)

# nb()