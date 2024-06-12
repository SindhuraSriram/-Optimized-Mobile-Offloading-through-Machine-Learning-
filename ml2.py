# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:25:22 2019

@author: Sindu Sreeram
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('i3_vid_ana_08feb.csv')
X = dataset.iloc[:,5].values
y = dataset.iloc[:,12].values
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('CPI,Memory,Cycles,instructions,cachemiss,time(Training set)')
plt.xlabel('Instructions')
plt.ylabel('Execution time')
plt.show()
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('CPI,Memory,Cycles,instructions,cachemiss,time(Test set)')
plt.xlabel('Instructions')
plt.ylabel('Execution time')
plt.show()