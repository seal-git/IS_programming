'''
Created on 2020/06/22

@author: tohoseal
'''
import numpy as np


if __name__ == '__main__':
    pass

n = [4,9,2]

'''
/s/:0, A:1, V:2, N:3, /e/:4
'''
W = np.zeros((5,5), dtype="float")

W[0][1] = (n[0]+9)/20 #1-1

W[0][2] = (n[1]+10)/20 #1-2

W[0][3] = (n[2]+11)/20 #1-3

W[1][3] = (n[0]+n[1])/20 #1-4

W[1][2] = (n[1]+n[2])/20 #1-5

W[2][3] = (n[0]+n[2])/20 #1-6

W[2][2] = (n[0]+4)/20 #1-7

W[3][3] = (n[1]+5)/20 #1-8

W[3][2] = (n[0]+6)/20 #1-9

W[3][4] = (n[0]+1)/20#1-10

W[2][4] = (n[1]+n[2])/20 #1-11

print(W)

W_AN = 1

W_VN = 0

W_NN = 0

W_AV = 0

W_VV = 0

W_NV = 0

L2 = np.array([[W_AN,W_VN,W_NN],[W_AV,W_VV,W_NV]])

print(L2)

W_sAVe = W_AV*W[2][4]

W_sNNe = W_NN*W[3][4]

L3 = np.array([W_sAVe, W_sNNe])

print(L3)

W[0][3] = W[0][3] + 1.0
W[0][1] = W[0][1] - 1.0
W[3][3] = W[3][3] + 1.0
W[1][3] = W[1][3] - 1.0

print(W)

