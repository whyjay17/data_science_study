# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 13:31:33 2017

@author: YJ
"""

# plotting tools
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import random

# Generate 100 random scores for three exams
df = pd.DataFrame(np.random.randint(0,100, size=(100, 1)), columns=['score'])

# Define grading rubric
def assign_grades(df):
    if df['score'] < 60:
        result = 'F'
    elif  60 <= df['score'] < 70:
        result = 'D'
    elif  70 <= df['score'] < 80:
        result = 'C'
    elif  80 <= df['score'] < 90:
        result = 'B'
    elif df['score'] >= 90:
        result = 'A'
    return result

def assign_status(df):
    if df['score'] % 2 == 0:
        result = 'In_state'
    else:
        result = 'Out_of_state'
    return result

# Assign letter grades residency status
df['letter_grade'] = df.apply(assign_grades, axis=1)
df['residency'] = df.apply(assign_status, axis=1)

# Examine the first few rows
df.head()

# generate hist based on score

ax = df['score'].plot(kind = 'hist', title = 'Histogram of Scores')

# examine how many students got a certain letter grade 
# (e.g., distribution by letter grades)

ax2 = df['letter_grade'].value_counts().plot(kind = 'bar', title = 'Distribution of Letter Grades')
ax2.set_xlabel("Letter")
ax2.set_ylabel("Frequency")

# plot residency status

ax3 = df['residency'].value_counts().plot(kind = 'bar')