# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 02:14:36 2017

@author: YJ
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# using seaborn lib

sns.set()

# Create Figure object that will allow us to control the global appearance

fig = plt.figure()

# Create Axes object : allows us to make an actual plot within our figure

ax = fig.add_subplot()

# shortcut

fig, ax = plt.subplots()

m = -2
b = 5
x = np.linspace(0, 10)
y = m * x + b

x2 = x
y2 = -1 * y

ax.plot(x, y, x2, y2)

ax.set_xlim(-2, 12)
ax.set_ylim(-20, 20)

# change how the numbers are displayed on the plot

ax.set_xticks(np.arange(0, 15, 5))
ax.set_yticks(np.arange(-15, 10, 5))

ax.set_xlabel("X")
ax.set_ylabel("Y")

# seaborn sepc modification

sns.set_context('poster')
sns.despine(offset = 10, trim = True)
sns.set_style("white")
sns.set_style("ticks")

plt.savefig('test.png')
plt.show()