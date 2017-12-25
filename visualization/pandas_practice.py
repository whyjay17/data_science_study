# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 01:55:59 2017

@author: YJ
"""

import os
import numpy as np
import pandas as pd

path = 'data/delta.csv'

# delta.csv: each row is aircraft, col is info

delta = pd.read_csv(path)

# iloc is-position based, loc is label-based

print(delta.iloc[5:10])
delta_iloc = delta.iloc[5:10]

print(delta.loc[5:10])
delta_loc = delta.loc[5:10]

airbus = delta[delta.Aircraft == 'Airbus A330-200']

# To obtain a particular cell value
# subset is Series

subset_example = delta["Wingspan (ft)"][delta.Aircraft == "Airbus A319"]
print(subset_example)

def get_value(df, col_name, aircraft_name):
    """
    Get the column value of a particular aircraft in the DataFrame.
    
    Parameters
    ----------
    df: A pandas DataFrame with similar structure to `delta_df`
    col_name: String
    aircraft_name: String
    
    Returns
    -------
    result: A float
    """
    
    return df[col_name][df.Aircraft == aircraft_name]

def get_summary(df, col_name):
    """
    Get the summary statistics of a particular column in the DataFrame.
    
    Parameters
    ----------
    df: A pandas DataFrame
    col_name: String
    
    Returns
    -------
    mean_value: Mean of column
    std_value: Standard deviation of column
    max_value: Max of column
    min_value: Min of column
    """
    
    return df.describe()[col_name]['mean'], df.describe()[col_name]['std'], df.describe()[col_name]['max'], df.describe()[col_name]['min']

def df_col_slice(df, list_of_columns):
    """
    Slice the DataFrame by a given list of column names.
    
    Parameters
    ----------
    df: A pandas DataFrame
    list_of_columns: List of columns names (String) to subset
    
    Returns
    -------
    result: A pandas DataFrame
    """
    
    frames = []
    
    for col in list_of_columns:
        frames.append(df[col])
    
    return pd.concat(frames, axis = 1)

def get_max_aircraft(df, col_name):
    """
    Get the aircraft name with the max value of some column in the DataFrame.
    
    Parameters
    ----------
    df: A pandas DataFrame with similar structure to `delta_df`
    col_name: String
    
    Returns
    -------
    result: Aircraft name (String)
    """
    
    return df.loc[df[col_name].idxmax()]['Aircraft']
    