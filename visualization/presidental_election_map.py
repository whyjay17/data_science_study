# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 04:30:42 2018

@author: YJ
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from nose.tools import assert_equal
from IPython.display import display_svg

"""
Visualize the results of the 2016 Presidental Election.
And the number of electoral votes on the map
"""

with open('../data/usa.svg') as f:
    usa = f.read()
    display_svg(usa, raw = True)
    
# ElectoralCollege2016.csv file contains
# the number of electoral votes for each state
# and who won

elec = '../data/ElectoralCollege2016.csv'

votes = pd.read_csv(elec, index_col = 'State') 

dem = '#698dc5' # a blue color
rep = '#f07763' # a red color

another_soup = BeautifulSoup(usa, 'xml')

res = {}

states = votes.index

for st in states:
    
    elec_votes = str(votes['ElectoralVotes'][st])
    winner = votes['WhoWon?'][st]
    
    res[st] = (winner, elec_votes)
    
    if st != 'ME-2':
        if res[st][0] == 'Clinton':
            another_soup.find('path', id = st)['fill'] = dem
        else:
            another_soup.find('path', id = st)['fill'] = rep
            
        p = another_soup.find('text', id = st)
        p.string = elec_votes
        
    else:
        ME2_id = another_soup.find('circle')['id']
        
        if res[ME2_id][0] == 'Clinton':
            another_soup.find('circle', id = ME2_id)['fill'] = dem

        else:
            another_soup.find('circle', id = ME2_id)['fill'] = rep


        p = another_soup.find('text', id = st)
        p.string = elec_votes
        
        
res_elec = another_soup.prettify()
display_svg(res_elec, raw = True)