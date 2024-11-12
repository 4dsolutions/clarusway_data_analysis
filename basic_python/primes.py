#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:24:20 2024

@author: kirbyurner

Trial by Division:
    
divide by all primes known so far 
up to where we know we're covered

Suggestion: use with itertools.islice

>>> from itertools import islice
>>> primes_gen = iter_prime() # defined below

>>> slice_of_primes = islice(primes_gen, 100, 201)

>>> next(slice_of_primes)
5869

>>> next(slice_of_primes)
5879

>>> next(slice_of_primes)
5881

Nov 8: added a generator function that returns
an iterator over primes.
"""

from math import sqrt, floor

primes = [2, 3]  # global to all

def isprime(n):
    limit = floor(sqrt(n))
    for p in primes:
        if p > limit:
            break
        if n % p == 0:
            return False
    return True

def nextprime():
    candidate = primes[-1]
    while True:
        candidate += 1
        if isprime(candidate):
            primes.append(candidate)
            break
    return candidate

def more(n):
    """
    Add n more prime numbers to primes
    
    Parameters
    ----------
    n : int
        how many more primes

    Returns
    -------
    None.

    """
    for _ in range(n):
        nextprime()
        
def iter_prime():
    "A generator function"
    yield 2
    yield 3
    while True:
        yield nextprime()
        
        
