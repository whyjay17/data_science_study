# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:36:01 2017

@author: YJ
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# num of variables used in plot = dimensionality of the plot

sns.set()

fig, ax = plt.subplots()

x = np.linspace(0, 100)
y1 = x + np.random.uniform(-10, 10, 50)
y2 = 100 - x + np.random.uniform(-10, 10, 50)

ax.scatter(x, y1, color = 'red', marker = 's', label = 'positive')
ax.scatter(x, y2, color = 'blue', marker = 'd', label = 'negative')

ax.plot(x, x, color = 'blue', linestyle = 'dashed', label = 'function')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

ax.set_xlim(-20, 120)
ax.set_ylim(-20, 120)

# Change the ticks on each axis and the corresponding numerical values that are displayed
ax.set_xticks(np.arange(0, 120, 20))
ax.set_yticks(np.arange(0, 120, 20))

ax.legend(loc = 'upper center')

ax.set_title("A complex correlation scatter plot!")
plt.show()