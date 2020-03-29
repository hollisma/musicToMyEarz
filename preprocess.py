#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Successfully Loaded")


# In[ ]:


# Read CSV
df = pd.read_csv("data/SpotifyFeatures.csv")
# df_top = df.head()

# df_top

df


# In[ ]:


df.dtypes


# In[ ]:


df['genre'].unique()


# In[ ]:


"""
Consolidate children's music. Two values for same category.
"""

print(np.sum(df['genre'] == "Children's Music"))
print(np.sum(df['genre'] == 'Children’s Music'))

new_gen = df['genre'].replace('Children’s Music', "Children's Music")


print(np.sum(new_gen == "Children's Music"))
print(np.sum(new_gen == 'Children’s Music'))

df['genre'] = new_gen.astype('category')


# In[ ]:


df['genre']


# ### Potential Issues:
# Changing keys into 0-1 columns may lead to underfitting, since there are more features and the same amount of data.
# 
# If a song is in a certain key, then there are 0's in all other columns of keys. In other words, the values of the columns of keys are dependent on the other such columns.

# In[ ]:


"""
Change keys into 0-1 columns
"""

df['key'].unique()
for k in df['key'].unique():
    # k == df['key'] gives boolean series
    df[k] = (k == df['key']).astype('int64')
    
df = df.drop(labels = 'key', axis = 'columns')


# In[ ]:


df.dtypes


# In[ ]:


df['time_signature'].unique()


# In[ ]:


"""
Change time signature into 0-1 columns
"""

for ts in df['time_signature'].unique():
    # k == df['key'] gives boolean series
    df[ts] = (ts == df['time_signature']).astype('int64')
    
df = df.drop(labels = 'time_signature', axis = 'columns')


# In[ ]:


df.dtypes


# In[ ]:


"""
Turn mode (major/minor) into a numerical column (0 for minor, 1 for major)
"""

df['mode'] = (df['mode'] == 'Major').astype('int64') 


# In[ ]:


df.dtypes


# In[ ]:


# histogram of popularity
pop = df['popularity'].to_numpy()

n, bins, patches = plt.hist(pop, bins = 50, density=False, facecolor='g')

plt.xlabel("popularity")
plt.ylabel("frequency")
plt.show()


# In[ ]:


# Separate larger dataframe into dataframes of all of one category
# dictionary that maps genre to the dataframe that only has songs of that genre
df_by_genre = dict()
for g in df['genre'].unique():
    df_by_genre[g] = df[df['genre'] == g]


# In[ ]:


# Find number of songs for each genre

for g,df_g in df_by_genre.items():
    print(g + ": " + str(df_g.shape[0]))

