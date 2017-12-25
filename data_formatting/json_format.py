# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 12:42:33 2017

@author: YJ
"""

import json

path = 'data/data.json'

with open(path, 'w') as fout:
    
    json.dump(airports, fout)