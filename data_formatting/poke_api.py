# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 00:29:50 2017

@author: YJ
"""

import requests, json
import csv

#url = "http://pokeapi.co/api/v2/ability/normalize/"
#res = requests.request('GET', url)
#json = res.json()

def pokeapi_request(request_type, name):
    '''
    Wrapper function to make an HTTP request to http://pokeapi.co/api/v2/request_type/name
    and returns the JSON response. The URL depends on the request_type.
    
    Parameters
    ----------
    request_type: String. Either "pokemon" or "ability"
    name: String.
    
    Returns
    -------
    result: A JSON string.
    '''
    
    url = 'http://pokeapi.co/api/v2/' + request_type + '/' + name
    res = requests.request('GET', url)
    
    return res.json()

def pokemons_ability(ability_name):
    '''
    Take an ability name and outputs a list of Pokemons with that ability.
    
    Parameters
    ----------
    ability_name: String. The name of the ability.
        
    Returns
    -------
    result: List. Name of all Pokemons with that ability.
    '''
    
    url = 'http://pokeapi.co/api/v2/ability/' + ability_name
    res = requests.request('GET', url)
    
    poke = []
    
    for pokemon in res.json()['pokemon']:
        
        poke.append(pokemon['pokemon']['name'])
    
    return poke
    
    
    