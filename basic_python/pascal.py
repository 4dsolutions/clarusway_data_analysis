#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:48:17 2024

@author: kirbyurner

Nov 18-19, 2024:  add numpy.array option + Pascal class iterator
"""

import numpy as np


def pascal():
    """
    generate Pascal's triangle row-by-row

    Yields
    ------
    row : list
        successive rows of Pascal's triangle.

    """
    row = [1] # starts here
    while True:
        yield row
        # e.g [0, 1, 3, 3, 1] + [1, 3, 3, 1, 0] = [1, 4, 6, 4, 1]
        row = [a + b for a, b in zip([0] + row, row + [0])]

def pascal2():
    """
    generate Pascal's triangle row-by-row using 
    numpy ndarrays -- looking ahead to Data Analysis

    Yields
    ------
    row : list
        successive rows of Pascal's triangle.

    """
    row = np.array([1]) # starts here
    zero= np.array([0])
    while True:
        yield row
        # e.g [0, 1, 3, 3, 1] + [1, 3, 3, 1, 0] = [1, 4, 6, 4, 1]
        # elementwise addition supported, so a simpler expression
        row =  np.hstack((row, zero)) + np.hstack((zero, row))        

class Pascal:
    """
    >>> op = Pascal()
    
    >>> next(op)
    [1]
    
    >>> next(op)
    [1, 1]
    
    >>> next(op)
    [1, 2, 1]
    
    >>> next(op)
    [1, 3, 3, 1]
    """
    
    def __init__(self):
        self.row = []
        
    def __next__(self):
        if not self.row:
            self.row = np.array([1])
            return self.row # first time only
        self.row = (np.hstack((self.row, np.array([0]))) +
                    np.hstack((np.array([0], self.row))))
        return self.row
    
    def __iter__(self):
        """
        you can iter() me but I'm already an iterator
        so I just return myself. Iterators should have
        both __next__ and __iter__.
        """
        return self

if __name__ == "__main__":
    # optionally use this syntax to call stuff when run top level
    help(__name__)