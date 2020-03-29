#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# print("Successfully Loaded modules for preprocess.py")








# ### Potential Issues:
# Changing keys into 0-1 columns may lead to underfitting, since there are more features and the same amount of data.
# 
# If a song is in a certain key, then there are 0's in all other columns of keys. In other words, the values of the columns of keys are dependent on the other such columns.



"""
Consolidate children's music. Two values for same category.
"""
def combine_child_music(df):
    new_gen = df['genre'].replace('Children’s Music', "Children's Music")
    df['genre'] = new_gen.astype('category')
    return df


"""
Change keys into 0-1 columns
"""
def keys_to_binary_cols(df):
    for k in df['key'].unique():
        # k == df['key'] gives boolean series
        df[k] = (k == df['key']).astype('int64')
        
    return df.drop(labels = 'key', axis = 'columns')


"""
Change time signature into 0-1 columns
"""
def time_sig_to_binary_cols(df):
    for ts in df['time_signature'].unique():
        # k == df['key'] gives boolean series
        df[ts] = (ts == df['time_signature']).astype('int64')
        
    return df.drop(labels = 'time_signature', axis = 'columns')


"""
Turn mode (major/minor) into a numerical column (0 for minor, 1 for major)
"""
def mode_to_binary_col(df):
    df['mode'] = (df['mode'] == 'Major').astype('int64')
    return df




"""
The function preprocesses the dataframe. Then returns a dictionary
of key: genre and value: dataframe of songs of only that genre

"""
def get_stratified_df():
    # Read CSV
    df_orig = pd.read_csv("data/SpotifyFeatures.csv")
    # list of functions that modify df
    funcs = [combine_child_music, keys_to_binary_cols, time_sig_to_binary_cols, mode_to_binary_col]
    df = df_orig
    for f in funcs:
        df = f(df)
    # Separate larger dataframe into dataframes of all of one category
    # dictionary that maps genre to the dataframe that only has songs of that genre
    df_by_genre = dict()
    for g in df['genre'].unique():
        df_by_genre[g] = df[df['genre'] == g]
    return df_by_genre

