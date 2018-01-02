# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:37:19 2017

@author: YJ
"""

def square_or_cube(values, incrementer='square'):
    """
    This function will either square all the elements of the values list or
    it will cube all the elements of the values list depending on if the 
    incrementer paramter is 'square' or 'cube'
    
    Parameters
    ----------
    values: list of integers to square or cube
    incrementer: string parameter that is either `square` or `cube` 
    
    Returns
    -------
    A list of integers
    """
    
    if incrementer == 'square':
        return list(map(lambda x : x ** 2, values))
    
    
    if incrementer == 'cube':
        print(list(map(lambda x : x ** 3, values)))
        return list(map(lambda x : x ** 3, values))
    
def filter_by_name_and_height(people):
    """
    Returns a list of people (i.e. dictionaries) that have names greater than 4 characters long
    and whose height is greater than 120 inches.
    
    Parameters
    ----------
    people: list of dictionaries
    
    Returns
    -------
    A list of dictionaries
    """
    
    # lambda with specified conditions:
    # names greater than 4 characters long
    # and whose height is greater than 120 inches.
    
    return list(filter(lambda x: len(x['name']) > 4 and x['height'] > 120, people))

#assert_array_equal(filter_by_name_and_height([
#    {'name': 'Andy', 'height': 180},
#    {'name': 'Bethany', 'height': 100},
#    {'name': 'Cassidy', 'height': 150}
#]), [{'name': 'Cassidy', 'height': 150}])

def reduce_wordcount(sentences):
    """
    Returns the number of characters in a list of strings
    
    Parameters
    ----------
    sentences: list of strings
    
    Returns
    -------
    An Integer
    """
    
    # concatenates all Strings using reduce and gets the length of that
    
    return len(reduce((lambda x, y: x + y), sentences))

#assert_equal(reduce_wordcount(['hello', 'word', 'nice']), len('hello')+len('word')+len('nice'))

def parse_seq(seq):
    '''
    parses an input sequence in string format to a list of strings (nucleotide triplets/codons)
    assumption: the length of the input string will always be divisble by 3
    
    Paramters
    ---------
    seq: String.
    
    Returns
    -------
    A list of strings (codons).
    '''
    
    # slices every 3 chars using list comprehension
    # makes use of the range with the for loop.
    
    return [
        seq[i : i + 3] for i in range(0, len(seq), 3)
    ]
    
def get_base_list(codons):
    '''
    takes a list of codons as input, counts each type of codon and 
    returns the individual bases/nucleotides as a list
    
    Paramters
    ---------
    codons: List of strings.
    
    Returns
    -------
    A list of characters (bases/nucleotides).
    '''
    
    return [char for item in codons for char in item]

print(get_base_list(parse_seq('ATATTAAAGAATAATTTTATAAAAATATGT')))
# ['A', 'T', 'A', 'T', 'T', 'A', 'A', 'A', 'G', 'A', 'A', 'T', 'A', 'A', 'T', 'T', 'T', 'T', 'A', 'T', 'A', 'A', 'A', 'A', 'A', 'T', 'A', 'T', 'G', 'T']

def transcribe(bases):
    '''
    Takes a DNA sequence and transcribes it into an RNA sequence i.e. substitutes 'T' bases with 'U'.
    
    Paramters
    ---------
    bases: List of characters (bases/nucleotides). Output from get_base_list().
    
    Returns
    -------
    A list of bases with 'T' substituted by 'U'.
    '''
    # substitutes all "T" nucleotides with "U" (Uracil) nucleotides and returns the substituted string as RNA sequence
    
    return [ 'U' if char == 'T' else char for char in bases]

print(transcribe(get_base_list(parse_seq('ATATTAAAGAATAATTTTATAAAAATATGT'))))