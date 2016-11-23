# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:37:40 2016

@author: abhnin
"""

def BinarySearch(L, e): # O(nlogn)
    
    L.sort() # Sort L in assending order
    
    low = 0
    high = len(L) -1
    
    while( high >= low ):
        
        mid = (low + high) // 2
        if(e == L[mid]):
            return True
        elif(e > L[mid]):
            low = mid + 1
        elif(e < L[mid]):
            high = mid - 1
            
    return False
    