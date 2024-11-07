#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:01:46 2024

@author: kirbyurner

Write a program that;
Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
the most frequent number was 3 and was repeated 4 times.

HINTS:
"""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

unique = set(numbers)
tally = {} # empty dict

for n in unique:
    tally[n] = numbers.count(n)
        
print(tally)

max(tally.values())

print("the most frequent number was {} and was repeated {} times")