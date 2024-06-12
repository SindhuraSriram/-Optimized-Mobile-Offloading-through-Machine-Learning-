# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:30:34 2019

@author: Sindu Sreeram
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('i3i5.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

