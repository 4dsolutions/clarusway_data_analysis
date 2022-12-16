import numpy as np
import math

N = 3

# rewrite of https://www.tutorialspoint.com/valid-sudoku-in-python
def isValidSudoku(M): 
    '''
    Check a sudoku matrix:
        A 9x9 sudoku matrix is valid iff every:
          row contains 1 - 9 and
          col contains 1 - 9 and
          3x3 contains 1 - 9
        0 is used for blank entry
    '''
    for i in range(9):
        row = {}
        col = {}
        block = {}
        row_cube = N * (i//N)
        col_cube = N * (i%N)
        for j in range(N*N):
            if M[i][j] != 0 and M[i][j] in row:
                return False
            row[M[i][j]] = 1
            if M[j][i] != 0 and M[j][i] in col:
                return False
            col[M[j][i]] = 1
            rc = row_cube + j//N
            cc = col_cube + j%N
            if M[rc][cc] in block and M[rc][cc] != 0:
                return False
            block[M[rc][cc]]=1
    return True
    
def generate_sudoku_puzzles(run_size, seed):  
    
    order = int(math.sqrt(run_size))
    count = 0
    valid = 0
    empty = []
    np.random.seed(seed) # for reproducible results
    
    for k in range(order):
        for l in range(order):

            A = np.fromfunction(lambda i, j: ((k*i + l+j) % (N*N)) + 1, (N*N, N*N), dtype=int)
            B = np.random.randint(2, size=(N*N, N*N))
            empty.append(np.count_nonzero(B))
            C = A*B
            count += 1

            if isValidSudoku(C):
                valid += 1
                last = C
                print('C(',k,l,') is valid sudoku:')
                print(C) # Uncomment for puzzle

    print('Tried', count, 'valid', valid, 'yield', round(valid/count, 3)*100, '%', 'Average Clues', round(sum(empty)/len(empty)))
    return(last)

posTest = np.array([(0, 7, 0, 0, 4, 0, 0, 6, 0), \
                    (3, 0, 0, 5, 0, 7, 0, 0, 2), \
                    (0, 0, 5, 0, 0, 0, 3, 0, 0), \
                    (0, 4, 0, 3, 0, 6, 0, 5, 0), \
                    (6, 0, 0, 0, 0, 0, 0, 0, 8), \
                    (0, 1, 0, 2, 0, 8, 0, 3, 0), \
                    (0, 0, 7, 0, 0, 0, 4, 0, 0), \
                    (1, 0, 0, 8, 0, 2, 0, 0, 9), \
                    (0, 6, 0, 0, 9, 0, 0, 1, 0), \
                    ])

negTest = np.array([(0, 7, 0, 0, 4, 0, 0, 6, 2), \
                    (3, 0, 0, 5, 0, 7, 0, 0, 2), \
                    (0, 0, 5, 0, 0, 0, 3, 0, 0), \
                    (0, 4, 0, 3, 0, 6, 0, 5, 0), \
                    (6, 0, 0, 0, 0, 0, 0, 0, 8), \
                    (0, 1, 0, 2, 0, 8, 0, 3, 0), \
                    (0, 0, 7, 0, 0, 0, 4, 0, 0), \
                    (1, 0, 0, 8, 0, 2, 0, 0, 9), \
                    (0, 6, 0, 0, 9, 0, 0, 1, 0), \
                    ])

print('Positive Quality Control Test:', isValidSudoku(posTest))
print('Negative Quality Control Test:', isValidSudoku(negTest))

print(generate_sudoku_puzzles(10000, 0))


