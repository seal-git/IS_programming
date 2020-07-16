'''
Created on 2020/05/16

@author: seal0
solve a simple Knapsack problem
w : weight
v: value
b: max_weight
N: num of bags
'''
import numpy as np

def solve_knapsack(w, v, b):
    N = len(w)
    idx = np.argsort(w)
    w = [w[i] for i in idx]
    v = [v[i] for i in idx]
    A = np.zeros((N+1, b+1), dtype=int)
    for i in range (1, N+1):
        for j in range (b+1):
            if(w[i-1] <= j):
                A[i][j] = max(v[i-1] + A[i-1][j-w[i-1]], A[i-1][j])
            else:
                A[i][j] = A[i-1][j]

    print(A)
    use_bag = []
    j = b
    for i in range(N, 0, -1):
        if(A[i][j] == A[i-1][j-w[i-1]]+v[i-1]):
            use_bag.append(idx[i-1])
            j = j - w[i-1]

    return (A[N][b], np.sort(use_bag))

