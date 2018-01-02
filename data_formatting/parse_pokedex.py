# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 03:24:01 2018

@author: YJ
"""

from IPython.display import display_html
from bs4 import BeautifulSoup

    
soup = BeautifulSoup(open('../data/pokedex.html', encoding = 'utf-8'), 'lxml')

poke_types = {}

rows = soup.body.table.find_all('tr')

for row in rows[1 : ]:
    
    for t in row.find_all('td')[2].find_all('a'):
        
        if t.text not in poke_types:
            poke_types[t.text] = []
        
        if row.find_all('td')[1].a.string not in poke_types[t.text]:
            poke_types[t.text].append(row.find_all('td')[1].a.string)