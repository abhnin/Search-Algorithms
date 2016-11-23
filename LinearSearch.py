# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:08:29 2016

@author: abhnin
"""

def LinearSearch(L, e):
    for element in L:
        if element == e:
            return True
    return False
    