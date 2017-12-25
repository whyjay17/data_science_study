# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:32:23 2017

@author: YJ
"""
# plotting tools
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

sentences = [["Let's","go","to","the","movies","this","weekend."],
             ["She","has","a","good","knowledge","of","history."],
             ["Move","the","vat","over","the","hot","fire."],
             ["I","have","a","new","pair","of","shoes."],
             ["You","still","need","to","write","a","report."],
             ["Today","has","been","a","very","long","day."]
            ]

# initialize 2x7 2D List
freq = [[0] * len(sentences[0]) for i in range(2)]

for j in range(len(sentences[0])):
    for i in range(len(sentences)):
        if sentences[i][j] == 'a':
            freq[0][j] += 1
        elif sentences[i][j] == 'the':
            freq[1][j] += 1
            
#printing the resulting frequency count in a readable manner

print('pos|\t', '\t'.join([str(x) for x in range(1, len(sentences[0]) + 1)]))
print('=' * 60)
articles = ['a', 'the']
i = 0

for row in freq:
    print(f'{articles[i]}|\t','\t'.join([str(score) for score in row]))#
    i += 1
    
# plot side-by-side

fig, ax = plt.subplots(1, 2, figsize = (6, 3))

pos = [x for x in range(1, len(sentences[0]) + 1)]

for i in range(2):
    
    """
    x = word position
    y = 'a' freq if i = 0
    y = 'the' freq if i = 1
    
    """
    
    ax[i].scatter(pos, freq[i])
    ax[i].set_xlabel('Word Pos')
    ax[i].set_ylabel('Word Counts')
    #ax[i].set_title(articles[i], 'Frequency')
    ax[i].set_xlim(0,len(sentences[0])+1)
    ax[i].set_ylim(-1,3) #max score + 1 : upper limit for y
