# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:44:33 2017

@author: YJ
"""

path = 'data/insulin_blastp.txt'

# takes a string, filename and returns the header as a list

def extract_header(filename):
    
    head_list = []
    
    with open(filename, 'r') as fin:
        for line in fin:
            line = line.replace('\n', '')
            head_list = line.split(',')
            break
    
    return head_list

def val_convert(filename, col):
    
    values = []
    
    with open(filename, 'r') as fin:
        
        lines = fin.readlines()[1:]
        
        for l in lines:
            values.append(l.strip().split(' ')[0].split('\t')[col])
            
    return values
