# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:11:29 2018

@author: YJ
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# import random forest family

from sklearn.ensemble import RandomForestRegressor

# import cross-validation pipeline

from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

# import evaluation metrics

from sklearn.metrics import mean_squared_error, r2_score

# import module for saving sckit-learn models
# joblib : alternative to pickle
from sklearn.externals import joblib

# load wine data from remote URL

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep = ';')

# (1599, 12): 1599 samples, 12 features

# Split data into training/test
# Separate target from training features

y = data.quality
X = data.drop('quality', axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, \
                                                    random_state = 123, stratify = y)

# It is a good practice to stratify your sample by the target variable
# this will ensure your training set looks similar to test set (more reliable)

# Standardation : process of subracting the means from each meature, then
# dividing by the feature std.dev 

"""
Fit the transformer on the training set (saving the means and standard deviations)
Apply the transformer to the training set (scaling the training data)
Apply the transformer to the test set (using the same means and standard deviations)
"""

# Fitting the Transformer API

scaler = preprocessing.StandardScaler().fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Pipeline with preprocessing and model

pipeline = make_pipeline(preprocessing.StandardScaler(), RandomForestRegressor(n_estimators = 100))

# Decalre hyper parameters to tune

hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}


# Cross-validation with pipeline

"""
GridSearchCV essentially performs cross-validation across the 
entire "grid" (all possible permutations) of hyperparameters.
"""

clf = GridSearchCV(pipeline, hyperparameters, cv=10)
 
# Fit and tune model
clf.fit(X_train, y_train)

# Use clf object as my model when applying it to other sets of data

y_pred = clf.predict(X_test)

# eval metrics

print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))

# Save model to a .pkl file
joblib.dump(clf, 'rf_regressor.pkl')

# loading model

clf2 = joblib.load('rf_regressor.pkl')
clf2.predict(X_test)