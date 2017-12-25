# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:11:16 2017

@author: YJ
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.subplots_adjust(wspace = 0.2, hspace = 0.3)

# a function to make a random scatter plot within the current subplot
def makePlot(ax, t, c):
    x = np.random.uniform(-5, 5, 100)
    y = np.random.uniform(-5, 5, 100)
    ax.scatter(x, y, color = c)
    ax.set_title(t)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_xticks(np.arange(-4, 5, 2))
    ax.set_yticks(np.arange(-4, 5, 2))
    
ax1 = fig.add_subplot(2, 2, 1)
makePlot(ax1, 'one', 'black')

ax2 = fig.add_subplot(2, 2, 2)
makePlot(ax2, 'two', 'red')

ax3 = fig.add_subplot(2, 2, 3)
makePlot(ax3, 'three', 'blue')

ax4 = fig.add_subplot(2, 2, 4)
makePlot(ax4, 'four', 'pink')