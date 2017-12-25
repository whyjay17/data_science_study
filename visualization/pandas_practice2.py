# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 02:04:19 2017

@author: YJ
"""

import os
import numpy as np
import pandas as pd

path = 'data/uniprot-mimivirus.tab'

df = pd.read_table(path, na_values = 'NaN')

def get_ec_with_dashes(df):
    '''
    Takes a pandas dataframe and returns a pandas.core.series.Series object containing EC numbers with dashes.
    
    Paramters
    ---------
    df: pandas DataFrame.
    
    Returns
    -------
    ec_dash_series: pandas.core.series.Series object. It should not return any other columns from df.
    '''
    
    dash_rows = df['EC number'].str.contains('-').fillna(False)
    return df['EC number'][dash_rows]

def rm_nan_go(df):
    '''
    Takes a pandas dataframe and returns a pandas dataframe object containing 
    only those rows that have non-null values in all three columns associated with gene ontology.
    
    Paramters
    ---------
    df: pandas DataFrame.
    
    Returns
    -------
    modified_df: pandas DataFrame. It must contain all columns from the original df.
    '''
    
    new_df = df.copy(deep = True)
    new_df = new_df.dropna(subset = ['Gene ontology (biological process)', 
                                    'Gene ontology (cellular component)', 
                                    'Gene ontology (molecular function)'])
    
    return new_df

def group_by_org(df):
    '''
    Takes a pandas dataframe and returns a pandas Series object containing 
    counts of 'Protein names' grouped by the 'Organism' column.
    
    Paramters
    ---------
    df: pandas DataFrame.
    
    Returns
    -------
    grouped_df: pandas Series object.
    '''
    
    return df.groupby(['Organism'])['Protein names'].count()

def add_column(df):
    '''
    Takes a pandas dataframe and returns a pandas dataframe object after adding the new column 'Size_Category'.
    
    Paramters
    ---------
    df: pandas DataFrame.
    
    Returns
    -------
    mod_df: pandas DataFrame.
    '''
    
    bins = [-np.inf, 300, 450, np.inf]
    labels = ['small','medium','large']
    mod_df = df.copy(deep = True)
    mod_df['Size Category'] = pd.cut(mod_df['Length'], bins = bins, labels = labels)
    
    return mod_df