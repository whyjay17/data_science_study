# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:07:04 2017

@author: YJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
This data set contains the quantity and species of the fish caught, 
what kind of gear was used as well as the number of permits, 
people and vessels involved in the process.
"""
path = 'data/ADFG_75_90.csv'

df = pd.read_csv(path, na_values = 'NaN', thousands = ',')

df = df[df.CONFIDENTIAL != 'CONFIDENTIAL']
df = df.drop('CONFIDENTIAL', 1)
df.describe(include =['O'])
df = df.dropna(axis=0, how='any') 

"""
we would be making use of jointplot() to create a scatterplot 
alongwith histograms at its margins. 
"""

def make_scatter_jointplot(x, y, df):
    '''
    Takes a pandas dataframe and returns a seaborn.axisgrid.JointGrid object for the scatter jointplot.
    
    Paramters
    ---------
    x: string. Column name for the x-axis.
    y: string. Column name for the y-axis.
    df: pandas DataFrame.
    
    Returns
    -------
    ax: A seaborn.axisgrid.JointGrid object
    '''
    
    return sns.jointplot(x = x, y = y, data = df, kind="kde")

"""
We can create a pairplot in order to visualize some of the pairwise 
relationships in our data set i.e. be able to guesstimate if there 
is a correlation and pursue further calculations, if there is any. 
"""

def make_pairplot(df, hue_column):
    '''
    Takes a pandas dataframe and returns a seaborn.axisgrid.PairGrid object for the pairplot.
    
    Paramters
    ---------
    df: pandas DataFrame.
    hue_column: string. Column name for the the hue parameter.
    
    Returns
    -------
    ax: A seaborn.axisgrid.PairGrid object
    '''
    # returns a PairGrid object that contains correponding values for the pairplot created
    
    return sns.pairplot(df, hue = hue_column)

"""
The FacetGrid class is useful when you want to visualize the 
distribution of a variable or the relationship between 
multiple variables separately within subsets of your dataset
"""

"""
In the following code cell, write a function named 
make_multi_pointplot() that takes df, a pandas DataFrame, 
col, the column that represents each of the five species, 
x and y, the x and y value columns to be supplied to the 
map function of the object FacetGrid.
"""

def make_multi_pointplot(df, col, x, y):
    '''
    Takes a pandas dataframe and returns a seaborn.axisgrid.FacetGrid object for the multiple pointplots.
    
    Paramters
    ---------
    df: pandas DataFrame.
    col: string. Column name from df whose values would also represent columns in the FacetGrid.
    x: string. Column name for specifying the x-axis in the map function.
    y: string. Column name for specifying the y-axis in the map function.
    
    Returns
    -------
    ax: A seaborn.axisgrid.FacetGrid object
    '''
    
    # col represents each of the five spieces
    ax = sns.FacetGrid(df, col = col)
    
    ax.map(sns.pointplot, x, y, ci = None)
    ax.add_legend()
    
    return ax

"""
We are interested in how many people used which kind of hear each year
to catch fish
"""

def make_heatmap(df, pivot_index, pivot_column, pivot_value):
    '''
    Takes a pandas dataframe and returns a matplotlib.axes._subplots.AxesSubplot object for the pairplot.
    
    Paramters
    ---------
    df: pandas DataFrame.
    pivot_index: string. The argument for `index` parameter in pivot_table().
    pivot_column: string. The argument for `columns` parameter in pivot_table().
    pivot_value: string. The argument for `values` parameter in pivot_table(). 
    
    Returns
    -------
    ax: matplotlib.axes._subplots.AxesSubplot
    '''
    # Create a pivot table
    
    piv_table = df.pivot_table(index = pivot_index, columns = pivot_column, \
                              values = pivot_value)
    
    ax = sns.heatmap(piv_table, cmap="YlGnBu")
    
    return ax