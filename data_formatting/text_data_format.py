# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:46:59 2017

@author: YJ
"""

import csv
import json


path = 'data/airports.csv'
path2 = 'data/data.csv'

airports = []

with open(path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter = ',')
    #next(reader)
    for row in reader:
        
        airports.append(row)
        

with open(path2, 'w') as csvfile:
    
    fout = csv.writer(csvfile, delimiter = '|')
    
    for airport in airports:
        
        fout.writerow(airport)
    
jsonpath = 'data/data.json'


with open(jsonpath, 'w') as fout:
    json.dump(airports, fout)

with open(jsonpath, 'r') as fin:
    data = json.load(fin)
    
print(data[:3])