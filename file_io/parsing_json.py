# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 21:18:23 2017

@author: YJ
"""

import json

def map_city_to_code(json_file):
    """
    Construct a dictionary mapping `code` to `name`
    
    Parameters
    ----------
    json_file: file path of json file
    
    Returns
    -------
    city_to_code: dictionary
    """
    
    city_to_code = {}
    
    with open(json_file, 'r') as jfile:
        
        data = json.load(jfile)
        
        for item in data['metros']:
            
            city_to_code[item['name']] = item['code']
            
    return city_to_code

def group_cities_by_continent(json_file):
    """
    Group cities by continent
    
    Parameters
    ----------
    json_file: file path of json file
    
    Returns
    -------
    cities_by_continent: dictionary
    """
    
    cities_by_continent = {}
    
    with open(json_file, 'r') as jfile:
        
        data = json.load(jfile)
        
        for item in data['metros']:
            
            # setdefault() will set dict[key]=default if key is not already in dict.
            
            cities_by_continent.setdefault(item['continent'], [])
            cities_by_continent[item['continent']].append(item['name'])
            
    return cities_by_continent
            

# Output json

jfile = 'data/map_data.json'

with open('data/map_data_out.json', 'w') as outfile:
    
    json.dump(group_cities_by_continent(jfile), outfile)
    
"""
will be reading in from a json file located at the variable: 
json_file and returning the k the most populous cities where 
k can be any integer that is a parameter into your function.
"""

def find_k_most_populous_cities(json_file, k):
    """
    Find k most populous cities
    
    Parameters
    ----------
    json_file: file path of json file
    k : integer
    
    Returns
    -------
    k_cities: array of strings
    """
    
    sorted_list = []
    pop_dict = {}
    
    with open(json_file, 'r') as jfile:
        
        data = json.load(jfile)
        
        for item in data['metros']:
            pop_dict[item['name']] = item['population']
            
    pop_dict = sorted(pop_dict.items(), key = lambda x : x[1], reverse = True)
    
    for elem in pop_dict:
        
        sorted_list.append(elem[0])
        
    return sorted_list[:k]