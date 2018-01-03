# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 02:25:07 2018

@author: YJ
"""

import pandas as pd
from bs4 import BeautifulSoup
from nose.tools import assert_equal
from IPython.display import display_svg

"""
Adds a new column 'Winner' based on
number of votes
"""


def winColumn(row):
    if row['후보자별 득표수'] > row['Unnamed: 7']:
        return '문재인'
    elif row['후보자별 득표수'] < row['Unnamed: 7']:
        return '홍준표'
    else:
        return ''

with open('../data/korea.svg', encoding = 'utf-8') as f:
    kor = f.read()
    display_svg(kor, raw = True)
    
soup = BeautifulSoup(kor, 'xml')

# color code

hong = '#C9151E'
moon = '#1870B9'

path = '../data/kor_elec.xlsx'

# vote data

df = pd.read_excel(path, index_col = '구시군명')

# format df

col_list = ['시도명','읍면동명','후보자별 득표수', 'Unnamed: 7']
df = df[col_list]
df['Winner'] = df[['후보자별 득표수','Unnamed: 7']].apply(winColumn, axis = 1)
df = df.dropna()

# Only include the Sum
df = df[df.읍면동명 == '합계']

# Add color to SVG image

soup = BeautifulSoup(kor, 'xml')

# List of Regions

# Temporary drop, TODO: fix this
df = df.drop(['고성군', '남구', '서구', '중구','강서구','동구','북구'])
regions = set(list(df.index.values))

for reg in regions:
    
    if df.loc[reg]['Winner'] == '문재인':
        try:
            soup.find('path', id = reg)['fill'] = moon
        except:
            continue
    else:
        try:
            soup.find('path', id = reg)['fill'] = hong
        except:
            continue
        
res_elec = soup.prettify()
display_svg(res_elec, raw = True)

        