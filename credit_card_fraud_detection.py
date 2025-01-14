# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zcy3aDPGxuw5TCX8esxWxCdazzaR-5UL
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

credit_data = pd.read_csv('/content/credit_card.csv')

# First 5 rows of the dataset
print(credit_data.head())

# Last 5 rows of the dataset
print(credit_data.tail())

# Info about the dataset
print(credit_data.info())

# Checking number of missing values in each column
print(credit_data.isnull().sum())

# Distribution of transactions
print(credit_data['Class'].value_counts())

# Separating the data for analysis
legit = credit_data[credit_data.Class == 0]
fraud = credit_data[credit_data.Class == 1]

print(legit.shape)
print(fraud.shape)

# Statistical data
print(legit.Amount.describe())
print(fraud.Amount.describe())

# Compare the values for both legit and fraud
print(credit_data.groupby('Class').mean())

legit_sample = legit.sample(n=52)

# Concatenate two dataframes
new_dataset = pd.concat([legit_sample, fraud], axis=0)

print(new_dataset.head())
print(new_dataset.tail())
print(new_dataset['Class'].value_counts())

# Splitting into features & target
X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

print(X)
print(Y)

# Split the data into training and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

# Model Training (Logistic Regression Model)
model = LogisticRegression()

# Training the LogisticRegression model
model.fit(X_train, Y_train)

# Evaluation (Based on accuracy score)
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Training Data Accuracy:', training_data_accuracy)

# Accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Test Data Accuracy:', test_data_accuracy)

# Function to take input and predict
def predict_transaction(model):
    input_data = []
    for column in X.columns:
        value = float(input(f"Enter value for {column}: "))
        input_data.append(value)
    
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    
    if prediction[0] == 0:
        print("The transaction is legitimate.")
    else:
        print("The transaction is fraudulent.")

# Taking user input and giving prediction
predict_transaction(model)
