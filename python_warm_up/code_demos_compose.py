#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:37:46 2023

@author: kirby urner
"""

def f(x):
    return 2 * x

def g(x):
    return x**2

arg = 10

print("f after g:", f(g(arg)))
print("g after f:", g(f(arg)))

class Compose:
    
    def __init__(self, a_function):
        "store a function"
        self.f = a_function
        
    def __call__(self, x):
        "call the stored function"
        return self.f(x)
    
    def __mul__(self, other):
        "compose stored function with another one"
        # self is callable
        return Compose(lambda x: self(other(x)))
    
# decorator syntax comes in handy in such cases
f = Compose(f)
g = Compose(g)

print("f after g:", (f * g)(arg))
print("g after f:", (g * f)(arg))

# using Compose as a class decorator
@Compose
def f(x):
    return 2 * x

# g will end up a Compose type object 
# with the function g saved internally
@Compose
def g(x):
    return x**2

print("f after g:", (f * g)(arg))
print("g after f:", (g * f)(arg))
