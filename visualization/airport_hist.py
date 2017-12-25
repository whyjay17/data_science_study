# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 13:39:39 2017

@author: YJ
"""

# plotting tools
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import random

path = 'data/airports.csv'

# creates a plot of the distribution of the airports by state

airports_df = pd.read_csv(path)

ax = airports_df['state'].value_counts().plot(kind = 'bar', \
                title='Distribution of Airports by State',figsize=(12,8))

def get_probability(df, state):
    """
    Compute the conditional probability P(visibility=X|Month=Y)
    
    Parameters
    ----------
    df: A Pandas DataFrame
    state: String. State abbrievation.
    
    Returns
    -------
    result: Float
    """
    
    return (df['state'].value_counts() / df['state'].count())[state]