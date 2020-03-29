#!/usr/bin/env python
# coding: utf-8

"""
train_rforestreg_whole returns the RandomForestRegressor
trained on the whole dataset.

The code to train RandomForestRegressors in random_forest.ipynb
has been omitted.

RandomForestRegressor trained on whole dataset yields a
better score.
"""



import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor

import preprocess
# preprocess has get_processed_df and get_stratified_df

import joblib

"""
Want to store model parameters of RandomForestRegressor

"""

"""
Labels: popularity
Attributes: features
"""
def get_attributes_labels(df):
    # remove genre, artist_name, track_name, track_id, popularity
    attribute_labels = df.columns[5:]

    attributes = []
    for a in attribute_labels:
        attributes.extend(list(df[a].values))

    attributes = np.asarray([np.asarray(attributes)])
    attributes = np.reshape(attributes, (len(attribute_labels), -1))
    attributes = attributes.transpose()

    labels = df['popularity'].values.reshape(-1, 1)
    
    return attributes, labels


""" 
Trains RandomForestRegressor on whole dataset
Returns RandomForestRegressor
"""
def train_rforestreg_whole():
    df = preprocess.get_processed_df()
    attributes, labels = get_attributes_labels(df)

    X_train, X_test, y_train, y_test = train_test_split(attributes, labels, test_size=0.2, random_state=0)
    rand_forest = RandomForestRegressor(n_estimators = 100, criterion = 'mse', max_depth = None, min_samples_split = 2)

    y_train = np.ravel(y_train)
    rand_forest.fit(X_train, y_train)
    return rand_forest

rand_forest = train_rforestreg_whole()
joblib.dump(rand_forest, 'rand_forest.joblib')
