# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:39:43 2017

@author: YJ
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# num of variables used in plot = dimensionality of the plot

sns.set()

fig, ax = plt.subplots()

x = np.linspace(0, 100)
y = x + np.random.uniform(-10, 10, 50)

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

ax.set_title("A positive correlation scatter plot!")

plt.show()