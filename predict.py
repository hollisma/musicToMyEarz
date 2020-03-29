"""
    Turn features dict into appropriate numpy array
    Load joblib file
    Do prediction
"""

import numpy as np
import joblib

"""
Given f, the dict of features, return the numpy array
with shape (1,28)
"""
def ft_dict_to_arr(f):
    arr = np.zeros((1,28), dtype=np.float64)
    ft_lst = ['acousticness', 'danceability', 'duration',
                'energy', 'instrumentalness', 'liveness',
                'loudness', 'mode', 'speechiness', 'tempo',
                'valence']
    for (i, field) in enumerate(ft_lst):
        arr[0][i] = f[field]
    # dict from key to corresponding index of array
    key_to_ind = {
        'C#' : 11,
        'F#' : 12,
        'C'  : 13,
        'F'  : 14,
        'G'  : 15,
        'E'  : 16,
        'D#' : 17,
        'G#' : 18,
        'D'  : 19,
        'A#' : 20,
        'A'  : 21,
        'B'  : 22
    }
    # f['key'] gives the song key of the user input
    # key_to_ind[f['key']] will give the index of the array
    # the corresponding entry is 1, the rest are 0
    arr[0][key_to_ind[f['key']]] = 1

    time_sig_to_ind = {
        4 : 23,
        5 : 24,
        3  : 25,
        1  : 26,
        0  : 27
    }
    arr[0][time_sig_to_ind[f['time_signature']]] = 1

    return arr


"""
Input: features, dict of features
Get the numpy array, do the prediciton on random forest,
return the predicted popularity value
"""

def predict_pop(features):
    # user_ft_arr should have shape (1,28)
    user_ft_arr = ft_dict_to_arr(features)
    rand_forest = joblib.load('rand_forest.joblib')
    prediction = rand_forest.predict(user_ft_arr)
    # prediction is a (1,) numpy array
    # Returns float value truncated to 3 decimal points
    return float('%.3f' % float(prediction[0]))