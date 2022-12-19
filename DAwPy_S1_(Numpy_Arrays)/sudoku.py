#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 10:10:02 2022

@author: Kirby Urner
"""

import numpy as np
from random import shuffle, choice
import time

zero_patch = np.zeros((3,3), dtype = int)
zero_to_eight = range(0, 9)

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
        
def recurse(board, nextpos=None, candidate=None):
    copy_board = board.copy()
    if nextpos:
        board[nextpos[0], nextpos[1]] = candidate
    # print(board)
    position = find_empty(board)
    if position:
        # print(position)
        candidates = list(range(1, 10))
        shuffle(candidates)
        for candidate in candidates:
            if check(board, candidate, position):
                # check if candidates left at this level
                return recurse(board, position, candidate)
        return copy_board # run out of candidates
    else:
        return board  # hit gold, no positions remain
    
def generate():
    attempt = 1
    start_time = time.time()
    B    = init_board()
    while True:
        print(attempt)
        newB = recurse(B)  # updates B until no more empty
        if not find_empty(newB):
            break
        B    = init_board()
        attempt += 1
    stop_time = time.time()
    the_time = stop_time - start_time
    print(f"Complete; Time: {the_time}")
    return newB

def solve(board):
    start_time = time.time()
    attempt = 0
    starting = board.copy()
    while True:
        # print(attempt)
        newB = recurse(starting)  # updates B until no more empty
        if not find_empty(newB):
            break
        attempt += 1
    stop_time = time.time()
    the_time = stop_time - start_time
    print(f"Solved; Time: {the_time}")
    return newB

def verify(board):
    print(np.sum(board, axis=0))
    print(np.sum(board, axis=1))
    panel_sums = []
    for vert_slice in np.vsplit(board, 3):
        for panel in np.hsplit(vert_slice, 3):
            panel_sums.append(np.sum(panel))
    print(panel_sums)
    
def redact(board, how_many=10):
    new_board = board.copy()
    coords = set()
    while len(coords) < how_many:
        coords.add((choice(zero_to_eight), choice(zero_to_eight)))
    rows = [pair[0] for pair in coords]
    cols = [pair[1] for pair in coords]
    new_board[rows, cols] = 0
    return new_board
    