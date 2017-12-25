# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 12:56:39 2017

@author: YJ
"""

import os
import csv

airport_data = []

# open csv and read it line by line

path = 'data/airports.csv'

with open(path) as file:
    
    reader = csv.reader(file, delimiter = ',')
    
    for row in reader:
        
        #print(row)
        
        airport_data.append(row)
     
"""
Create a function called airport_count() that takes a list of list obtained 
from a CSV (i.e., airport_data) and a state abbreviation (e.g. "IL") 
and outputs the number of airports in that particular state.
"""
        
def airport_count(airport_data, state_abbr):
    """
    Get the column value of a particular aircraft in the DataFrame.
    
    Parameters
    ----------
    airport_data: List of list
    state_abbr: String
    
    Returns
    -------
    result: Count of airports (Int)
    """
    
    counter = 0
    
    for dat in airport_data:
        
        if dat[3] == state_abbr:
            
            counter += 1
            
    return counter


"""
Create a function called write_state_count() which takes a directory path 
and outputs a csv file that contains two columns: (1) state_abbreviation, 
and (2) airport_count. Use a semi-colon as the delimiter for this 
file (i.e., ";"). Do not create a header.
"""

# List of state abbreviations
state_abbr = ["AK","AL","AR","AS","AZ","CA","CO","CQ","CT","DC","DE","FL","GA","GU",
              "HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO",
              "MS","MT","NA","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR",
              "PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV",
              "WY"]

def write_state_count(file_path):
    """
    Create a csv file at the specific file path which counts the airports of each states.
    
    Parameters
    ----------
    file_path: String. Path to CSV file.
    
    Returns
    -------
    None
    """
    
    with open(file_path, 'w+') as csvfile:
        
        writer = csv.writer(csvfile, delimiter = ',')
        for state in state_abbr:
            writer.writerow([state, airport_count(airport_data, state)])
            
"""
Write a function called parse_weather() which takes in the CSV file 
and a month value. The function will output the average visibity score 
for that particular month.
"""

def parse_weather(csv_file, month):
    """
    Read a CSV file and returns the titles after specified year.
    
    Parameters
    ----------
    csv_file: String. Path to CSV file.
    month: Int.

    Returns
    -------
    result = Float.
    """
    
    counter = 0
    vis_sum = 0
    
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row in reader:
            if int(row[1]) == month:
                counter += 1
                vis_sum += float(row[5])
                
    return vis_sum / counter
                