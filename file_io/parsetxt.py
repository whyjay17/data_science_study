# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:14:27 2017

@author: YJ

Basic parsing practice

"""

path = 'data/airport.txt'

# read file, return a dictionary of airport city to city mappings

def construct_map(filepath):
    
    map_dict = {}

    # any files opened will be closed automatically after you are done    
    with open(filepath, 'r') as fin:
        
        for line in fin:
            
            line = line.replace('\n', '')
            
            # split the line based on space
            
            cols = line.split(' ')
            #print(cols)
            
            map_dict[cols[0]] = ' '.join(cols[1: ])
    
    return map_dict
