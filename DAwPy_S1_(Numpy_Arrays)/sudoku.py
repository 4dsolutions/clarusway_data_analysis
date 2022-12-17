#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:10:02 2022

@author: mac
"""

import numpy as np
from random import shuffle
import time

zero_patch = np.zeros((3,3), dtype = int)

def init_board():
    
    def diag_patch():
        one_nine = list(range(1, 10))
        shuffle(one_nine)
        return np.array(one_nine, dtype=int).reshape(3,3)
    
    row0       = np.concatenate([diag_patch(), 
                                 zero_patch, 
                                 zero_patch], axis = 1)
    
    row1       = np.concatenate([zero_patch, 
                                 diag_patch(), 
                                 zero_patch], axis = 1)
    
    row2       = np.concatenate([zero_patch, 
                                 zero_patch, 
                                 diag_patch()], axis = 1)
    
    board      = np.concatenate([row0, row1, row2], axis=0)
    
    return board

def find_empty(board):
    rtnval = False
    results = np.where(board == 0)
    if results[0].size > 0:
        rtnval = [results[0][0], results[1][0]]
    return rtnval

def check(board, value, pos):
    
    def in_patch(r, c):
        if 0 <= row <= 2:
            patch_row = 0
        if 3 <= row <= 5:
            patch_row = 3
        if 6 <= row <= 9:
            patch_row = 6   
        if 0 <= col <= 2:
            patch_col = 0
        if 3 <= col <= 5:
            patch_col = 3
        if 6 <= col <= 9:
            patch_col = 6    
        
        return value in board[patch_row:patch_row+3,
                              patch_col:patch_col+3]
            
    row, col = pos
    if value in board[row] or value in board[:,col]:
        return False
    if in_patch(row, col):
        return False
    return True
        
def recurse(board):
    position = find_empty(board)
    if position:
        for candidate in range(1, 10):
            if check(board, candidate, position):
                board[position[0], position[1]] = candidate
                # print(board)
                return recurse(board)
        # print("Unsolved")
        return False
    else:
        return True

def generate():
    attempt = 0
    start_time = time.time()
    while True:
        # print(attempt)
        B = init_board()
        if not recurse(B):  # updates B until no more empty
            attempt += 1
            continue        # dead end, try new B
        break  # solution found
    stop_time = time.time()
    the_time = stop_time - start_time
    print(f"Solved; Time: {the_time}")
    return B

def verify(board):
    print(np.sum(board, axis=0))
    print(np.sum(board, axis=1))
    panel_sums = []
    for vert_slice in np.vsplit(board, 3):
        for panel in np.hsplit(vert_slice, 3):
            panel_sums.append(np.sum(panel))
    print(panel_sums)