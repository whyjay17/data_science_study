# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 01:00:08 2017

@author: YJ
"""

# We need to import the math library for the ceil method, which returns the next largest 
# integer to a floating point value
import math as mt

# We want to loop from 10 to 100,000,000
for i in range(1,8):
    
    # Now print out the integer value, and the number of bins
    # We used a math trick here, 10**i**(1/3) = 10**(i/3)
    print("%9d\t%4d\n" % (10**i, mt.ceil(pow(10, i/3.))))
    
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(0, 100, 10000)
y = x + np.random.uniform(-10, 10, 10000)

ax.hist(y)

#plt.show()

# multiple histograms

fig2 = plt.figure(figsize=(12, 8))
ax2 = fig2.add_subplot(111, facecolor = 'Ivory')

# Now we generate something to plot. In this case, we will need data 
# that are randomly sampled from a particular function.

x2 = np.linspace(0,100, 10000)
y1 = x2 + np.random.uniform(-10, 10, 10000)
y2 = x2 + np.random.uniform(-25, 25, 10000)
y3 = x2 + np.random.uniform(-35, 35, 10000)

ax2.hist((y1, y2, y3), bins = 15, histtype = 'bar', normed = True, \
         color=('BurlyWood', 'IndianRed', 'DeepSkyBlue'), label=('Type A', 'Type B', 'Type C'))

# Complete the plot

ax2.set_title("Histogram")
ax2.set_xlabel("Value")
ax2.set_ylabel("Probability")
ax2.set_xlim(-45, 145)
ax2.legend()
plt.show()