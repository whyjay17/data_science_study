# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:11:10 2017

@author: YJ
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# num of variables used in plot = dimensionality of the plot

sns.set()

fig, ax = plt.subplots()

# 50 linearly spaced x vals

x = np.linspace(0, 100)

# 50 y vals linearly related to x

y = x + np.random.uniform(-10, 10, 50)

# outliers

y[2] = 60
y[6] = 75

ax.scatter(x, y)

# Set our axis labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# Change the axis limits displayed in our plot
ax.set_xlim(-20, 120)
ax.set_ylim(-20, 120)

# Change the ticks on each axis and the corresponding numerical values that are displayed
ax.set_xticks(np.arange(0, 120, 20))
ax.set_yticks(np.arange(0, 120, 20))
    
ax.set_title("An outlier detection scatter plot!")

plt.show()