# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:34:34 2017

@author: YJ
"""

import xml.etree.ElementTree as ET

example_string = '''<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="children">
    <title>Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title>Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>'''

books = ET.fromstring(example_string)

for book in books.iter('year'):
    print(book.text)
    
sum_price = 0

for price in books.iter('price'):
    sum_price += float(price.text)
    
print(sum_price)

# But what if we want to access the attribute "category" of the 
# element "book"?

for book in books:
    print('Accessing key-val tuple as a list: {0}'.format(book.items()))
    print('Attribute key: {0}'.format(book.items()[0][0]))
    print('Attribute val: {0}'.format(book.items()[0][1]))
    
example_string2 = '''<?xml version="1.0" encoding="UTF-8"?>
<books>
<title>Harry Potter and the Sorcerer's Stone</title>
<title>Harry Potter and the Chamber of Secrets</title>
<title>Harry Potter and the Prisoner of Azkaban</title>
<title>Harry Potter and the Goblet of Fire</title>
<title>Harry Potter and the Order of the Phoenix</title>
<title>Harry Potter and the Half-Blood Prince</title>
<title>Harry Potter and the Deathly Hallows</title>
</books>
'''

book_series = ET.fromstring(example_string2)

for book in book_series:
    print(book.text[21:])
    
keyword_string1 ='''<?xml version="1.0" encoding="UTF-8"?>
<entries>
    <keyword id="KW-0002">3D-structure</keyword>
    <keyword id="KW-0181">Complete proteome</keyword>
    <keyword id="KW-0342">GTP-binding</keyword>
    <keyword id="KW-0378">Hydrolase</keyword>
    <keyword id="KW-0489">Methyltransferase</keyword>
    <keyword id="KW-0506">mRNA capping</keyword>
    <keyword id="KW-0507">mRNA processing</keyword>
    <keyword id="KW-0511">Multifunctional enzyme</keyword>
    <keyword id="KW-0547">Nucleotide-binding</keyword>
    <keyword id="KW-0548">Nucleotidyltransferase</keyword>
    <keyword id="KW-1185">Reference proteome</keyword>
    <keyword id="KW-0694">RNA-binding</keyword>
    <keyword id="KW-0949">S-adenosyl-L-methionine</keyword>
    <keyword id="KW-0808">Transferase</keyword>
    <keyword id="KW-0946">Virion</keyword>
</entries>'''.strip()

# Return the value of the id attributes

ids = ET.fromstring(keyword_string1)

for i in ids.iter('keyword'):
    print(i.get('id'))
    
ec_string1 = '''<?xml version="1.0" encoding="UTF-8"?>
<entries>
    <protein>
        <recommendedName>
            <fullName>Nucleoside diphosphate kinase</fullName>
            <shortName>NDK</shortName>
            <shortName>NDP kinase</shortName>
            <ecNumber>2.7.4.6</ecNumber>
        </recommendedName>
    </protein>
    <protein>
        <recommendedName>
            <fullName>Tyrosine--tRNA ligase</fullName>
            <ecNumber>6.1.1.1</ecNumber>
        </recommendedName>
        <alternativeName>
            <fullName>Tyrosyl-tRNA synthetase</fullName>
            <shortName>TyrRS</shortName>
        </alternativeName>
    </protein>
</entries>
'''.strip()

# return ecNumber

ecList = []

xml_str = ET.fromstring(ec_string1)

for st in xml_str.iter('recommendedName'):
    print(st.find('ecNumber').text)
    ecList.append(st.find('ecNumber').text)
    
hits_string1 = '''<?xml version="1.0" encoding="UTF-8"?>
<entries>
    <Hit>
      <num>39</num>
      <hsps>
        <Hsp>
          <num>1</num>
          <bit-score>70.2005</bit-score>
          <score>158</score>
          <evalue>1.2971e-14</evalue>
          <identity>20</identity>
          <positive>20</positive>
          <query-from>1</query-from>
          <query-to>21</query-to>
          <hit-from>1</hit-from>
          <hit-to>21</hit-to>
          <align-len>21</align-len>
          <gaps>0</gaps>
          <qseq>GIVEQCCTSICSLYQLENYCN</qseq>
          <hseq>GIGEQCCTSICSLYQLENYCN</hseq>
          <midline>GI EQCCTSICSLYQLENYCN</midline>
        </Hsp>
      </hsps>
    </Hit>
    <Hit>
      <num>40</num>
      <hsps>
        <Hsp>
          <num>1</num>
          <bit-score>75.2903</bit-score>
          <score>170</score>
          <evalue>1.31e-14</evalue>
          <identity>21</identity>
          <positive>21</positive>
          <query-from>1</query-from>
          <query-to>21</query-to>
          <hit-from>77</hit-from>
          <hit-to>97</hit-to>
          <align-len>21</align-len>
          <gaps>0</gaps>
          <qseq>GIVEQCCTSICSLYQLENYCN</qseq>
          <hseq>GIVEQCCTSICSLYQLENYCN</hseq>
          <midline>GIVEQCCTSICSLYQLENYCN</midline>
        </Hsp>
      </hsps>
    </Hit>
    <Hit>
      <num>41</num>
      <hsps>
        <Hsp>
          <num>1</num>
          <bit-score>75.2903</bit-score>
          <score>170</score>
          <evalue>1.32111e-14</evalue>
          <identity>21</identity>
          <positive>21</positive>
          <query-from>1</query-from>
          <query-to>21</query-to>
          <hit-from>78</hit-from>
          <hit-to>98</hit-to>
          <align-len>21</align-len>
          <gaps>0</gaps>
          <qseq>GIVEQCCTSICSLYQLENYCN</qseq>
          <hseq>GIVEQCCTSICSLYQLENYCN</hseq>
          <midline>GIVEQCCTSICSLYQLENYCN</midline>
        </Hsp>
      </hsps>
    </Hit>
</entries>'''.strip()

def get_avg_score(xml):
    '''
    Takes entries of BLAST hits and returns the average based on the scores
    (contained in the "score" element) of each entry.
    
    Paramters
    ---------
    xml: String. An XML format string.
    
    Returns
    -------
    avg_score: float. The average of score in every 'hit' in the XML string.
    '''
    
    xml_str = ET.fromstring(xml)
    
    total_score = 0
    length = 0
    
    for xml in xml_str.iter('Hsp'):
        total_score += int(xml.find('score').text)
        length += 1

        
    return total_score / length
    
    
