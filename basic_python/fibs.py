#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 06:14:48 2024

@author: kirbyurner

https://mathworld.wolfram.com/FibonacciNumber.html

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 
233, 377, 610, 987, 1597, 2584, 4181, 6765, 
10946, 17711, 28657, 46368, 75025, 121393, 
196418, 317811, 514229, 832040, 1346269, 
2178309, 3524578, 5702887, 9227465, 14930352, 
24157817, 39088169, 63245986, 102334155
"""

def fibs():
    """
    generate the Fibonacci sequence
    """
    yield 0
    yield 1
    yield 1
    seed = [1, 1]
    while True:
        seed += [sum(seed[-2:])] # extend
        yield seed[-1]  # yield rightmost
        seed = seed[1:] # drop leftmost
        