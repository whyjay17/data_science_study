# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 01:15:28 2017

@author: YJ
"""

"""
Pandas introduces several new data structures like
Series, DataFrame, Panel that build on top of numpy
to speed up data analysis task.
"""

import pandas as pd
import numpy as np

"""
Series: a 1-d labeled array that can hold any data type
It has both data column and a label column called index
"""

s1 = pd.Series(np.random.rand(4), index = ['a', 'b', 'c', 'd'])

d = {'a' : 11, 'b' : 21, 'c': 34, 'd': 32}
s2 = pd.Series(d)#, index = ['c', 'y'])

s3 = pd.Series(34, index = ['a', 'b'])


"""
DataFrame: a 2-d labeled data structure with cols that can
be hold different data types. Similar to tables
"""

path = 'data/grades.csv'

dfa = pd.read_csv(path)

# grab first five rows and only extract grade col

print(dfa.head(5))

# We can also perform numerical operations on a DataFrame, just as was the case with NumPy arrays.

df = pd.DataFrame(np.random.randn(5, 6))
df + 2.5