# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:30:59 2018

@author: YJ
"""

# We use BeautofulSoup version 4
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('test.html'), 'lxml')

# Now lets print out the start of the HTMl file
print(soup.prettify()[:108])

print('title element = ', soup.title)
print('title value = ', soup.title.string)
print('title parent element = ', soup.title.parent.name)
print('body class attribute = ', soup.body['class'])
print('ul ', soup.ul)

# find all occurances of p

for elem in soup.find_all('p'):
    print(elem)
    
soup.title.string = 'New Title!!'
# Now lets print out the start of the HTMl file
print(soup.prettify()[:108])

print(soup.select('p[align]'))
print(soup.select('p[type]'))

"""
While Beautiful Soup provides a great deal of power and 
simplicity in DOM parsing and element retrieval, 
the full power of parsing a document requires the use of 
regular expressions.
"""


"""
html = '''
<!DOCTYPE html>
<html>
<head id='hid' class='hclass'>
<title> Test, this is only a test ... </title>
</head>
<body id='bid' class='bclass'>
<header> 
This is text in the header.
</header>

<h2 color='mycolor'>This is a Header Level 2</h2>

<p align='myalign'>Here is some text in a paragraph.</p>

<p> Here is a list </p>
<ul id='ulid'>
<li> List Item #1 </li>
<li> List Item #2 </li>
</ul>

<p type='caption'> Here is a table </p>
<table id='tid'>
<tr>
<th> Column #1 </th>
<th> Column #2 </th>
</tr>
<tr>
<td> A value </td>
<td> Another Value </td>
</tr>
</table>

<p> Some concluding text </p>

<footer>
<hr />
This is a text in the footer.
</footer>

</body>
</html>
'''

# Now save the HTML string
with open('test.html', 'w') as fout:
    fout.write(html)
"""