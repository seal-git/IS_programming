'''
Created on 2020/05/16
@author: seal0
'''
'''
Judge if sum of combination of A={a1, a2, ..., an} can make N by using DP
Order of this algorithm is O(Nn)
'''

import numpy as np

# set N, A={a1, a2, ..., an}
N = 354
A = [1, 2, 5, 8, 12, 45, 133]

#set matrix M: num of row is size of A+1, num of column is N+1
M = np.zeros((len(A)+1, N+1), dtype=int)

#set answer when A is empty
M[0] = [1 if (i==0) else 0 for i in range(0, N+1)]

#fill in all cells
for i in range(len(A)):
    for j in range(N+1):
        if(j < A[i]):
            M[i+1][j] = M[i][j]
        elif(j == A[i]):
            M[i+1][j] = 1
        elif(j > A[i]):
            M[i+1][j] = M[i][j-A[i]]

#output result
if(M[len(A)][N]==1):
    print("Yes")
else:
    print("No")