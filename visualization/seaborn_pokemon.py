# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 15:32:13 2017

@author: YJ
"""

import matplotlib as mpl
import numpy as np
from numpy.testing import assert_array_equal
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

path = 'data/pokemon.csv'

df = pd.read_csv(path, encoding='latin-1', index_col = 0)

df.head()

# Attack vs Defense

"""
In this problem we will create a simple linear regression plot using 
[lmplot](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot) 
between the Attack statistics and the Defense statistics of pokemon.
"""
def lm_plot():
    lm_plot = sns.lmplot('Attack', 'Defense', df, hue = 'Stage', size = 10)
    lm_plot.set(xlim = (0, 160))
    lm_plot.set(ylim = (0, 200))

# Attack of Different Types

"""
We will see how the Attack of different Pokemon are spread across
based on their types
"""

# Defining the color palette
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

# Violin Plot
def violin_plot():
    violin_ax = sns.violinplot(size = 15, x = 'Type 1', y = 'Attack', data = df, palette = pkmn_type_colors)
    violin_ax.set(ylim=(-40.0, 220.0))
    
# Swarm Plot
def swarm_plot():
    swarm_ax = sns.swarmplot(size = 11, x = 'Type 1', y = 'Attack', data = df, palette = pkmn_type_colors)
    
# Advanced Swarm Plot

def advanced_swarm_plot(df):
    """
    Plots an advanced swarm plot based on each stat
    for each type.

    Parameters
    ----------
    
    df : dataframe of 151 Pokemon
    
    Returns
    -------
    a matplotlib.axes._subplots.AxesSubplot instance
    
    """
    # Set figsize to (20, 7)
    
    plt.figure(figsize=(20, 7))
    
    # Preprocess : remove the 'Total', 'Stage' and 'Legendary'
    
    df = df.drop(['Total', 'Stage', 'Legendary'], axis = 1)
    
    # use the melt() function of pandas, only keep the "Name", "Type 1" and "Type 2"

    df = pd.melt(df, id_vars=['Name', 'Type 1', 'Type 2'], var_name='Stat')
    
    return sns.swarmplot(x = 'Stat', y = 'value', hue = 'Type 1', data = df)