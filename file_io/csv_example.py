# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 18:10:21 2017

@author: YJ
"""

# plotting tools
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

path = 'data/grades.csv'

"""
Will be reading file at 'path' and construct x and y vals 
that will be plotting. Each line in csv : year and grades
Needs to ignore header. 
"""

# Returns two arrays: years and avg_grades

def construct_values(path):
    
    """
    Construct the values needed to graph the average grade of the class over time
    
    Parameters
    ----------
    file_path: A string. Absolute path to file.
    
    Returns
    -------
    years: array of integers
    average_grades: array of floats
    """
    
    years, grades = [], []
    val_dict = {}
    colNum_dict = {}
    
    with open(path) as file:
        reader = csv.reader(file, delimiter = ',')
        
        # Skip header
        next(reader)
        
        for row in reader:
            if row[0] not in val_dict.keys():
                val_dict[row[0]] = float(row[1])
                colNum_dict[row[0]] = 1
            else:
                val_dict[row[0]] += float(row[1])
                colNum_dict[row[0]] += 1
            #break
        
        for item in val_dict:
            val_dict[item] /= colNum_dict[item]
            years.append(item)
            grades.append(val_dict[item])
        
    return years, grades

def plot_grades(path):
    
    """
    Plots the average grades over time as a scatter plot
    
    Parameters
    ----------
    file_path: A string. Absolute path to file.
    
    Returns
    -------
    A matplotlib.Axes instance.
    """
    
    year, avg = construct_values(path)
    fig, ax = plt.subplots()
    
    ax.set_xlim(2000, 2018)
    ax.plot(year, avg, marker = 'o', color = 'r', linestyle = 'none')
    ax.margins(x=0)
    plt.show()
    

plot_grades(path)
    