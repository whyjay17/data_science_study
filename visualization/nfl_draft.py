# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 04:00:55 2018

@author: YJ
"""

import numpy as np
from numpy.testing import assert_array_equal
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib as mpl
import matplotlib.pyplot as plt

# Define the URL
draft_url = "https://www.pro-football-reference.com/years/2017/draft.htm"

html = urlopen(draft_url)

soup = BeautifulSoup(html, 'lxml')

# col headers

column_headers = [val.getText() for val in soup.findAll('tr', limit = 2)[1].findAll('th')]

# Ignore the round
column_headers.pop(0)

# Obtain the drafted players table based on the tag "#drafts tr" after the header
table_rows = soup.select("#drafts tr")[2:] 

# Player_data is a list of list where each element is a list of data
# Extract all player data
player_data = [[td.getText() for td in table_rows[i].findAll('td')] for i in range(len(table_rows))]

# Create a Pandas DataFrame from the list of list
df_2017 = pd.DataFrame(player_data, columns=column_headers)

# Drop last column which is just a link
df_2017 = df_2017.drop(labels='', axis=1)

# Preview table
df_2017.head()

"""
Create visualization based on the draft data
Distribution of the age of each players in the draft
"""

freq_age = df_2017.groupby(['Age']).size()
freq_age.plot(kind = 'bar')
plt.show()

def freq_plot(df, col_name):
    """
    Create a frequency plot
    
    Parameters
    ----------
    df: Pandas DataFrame.
    column_name: String. Name of column.
    
    Returns
    -------
    ax: A matplotlib.Axes instance.
    """
    fig, ax = plt.subplots()
    freq = df.groupby(col_name).size()
    
    freq.plot(kind = 'bar')
    
    plt.title('Dist of ' + col_name)
    plt.show()
    
    return ax
    

freq_plot(df_2017, 'College/Univ')
freq_plot(df_2017, 'Pos')

"""
Takes a Pandas df and college name and return the 
number of players drafted from that college
"""

def draft_count(df, college_name):
    """
    Count number of drafts from a specified college
    
    Parameters
    ----------
    df: Pandas DataFrame. Same format as in the example above.
    college_name: String. Name of college.
    
    Returns
    -------
    result: Int. Number of players drafted from specific college.
    """
    
    return (df['College/Univ'] == college_name).sum()

    