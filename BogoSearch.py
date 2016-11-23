# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:56:20 2016

@author: abhnin
"""
import random

def BogoSearch(L, e):
    length = len(L)
    while True:
        random_index = random.randint(0, length-1)
        if(L[random_index] == e):
            return True
    
    
    