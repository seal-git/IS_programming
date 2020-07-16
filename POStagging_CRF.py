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

W[1][2] = (n[0]+n[1])/20 #1-4

W[1][3] = (n[1]+n[2])/20 #1-5

W[2][3] = (n[0]+n[2])/20 #1-6

W[2][2] = (n[0]+4)/20 #1-7

W[3][3] = (n[1]+5)/20 #1-8

W[3][2] = (n[0]+6)/20 #1-9

W[3][4] = (n[0]+1)/20#1-10

W[2][4] = (n[1]+n[2])/20 #1-11

print(W)

alpha = {}

W_sx = {}
W_sx["sA"] = np.exp(1*W[0][1])
W_sx["sV"] = np.exp(0*W[0][2])
W_sx["sN"] = np.exp(0*W[0][3])
W_xe = {}
W_xe["Ne"] = np.exp(1*W[3][4])
W_xe["Ve"] = np.exp(0*W[3][4])

W_xx = {}
W_xx["AN"] = np.exp(W_sx["sA"])*np.exp(W_xe["Ne"])
W_xx["AV"] = np.exp(W_sx["sA"])*np.exp(W_xe["Ve"])
W_xx["VN"] = np.exp(W_sx["sV"])*np.exp(W_xe["Ne"])
W_xx["VV"] = np.exp(W_sx["sV"])*np.exp(W_xe["Ve"])
W_xx["NN"] = np.exp(W_sx["sN"])*np.exp(W_xe["Ne"])
W_xx["NV"] = np.exp(W_sx["sN"])*np.exp(W_xe["Ve"])

print("W_xx")
for i in W_xx:
    print(i, ":", W_xx[i])

sum_W_xx = sum(W_xx.values())
P_xx = {}
for key in W_xx.keys():
    P_xx[key] = W_xx[key]/sum_W_xx

print("P_xx")
print(sum(P_xx.values()))
for i in P_xx:
    print(i, ":", P_xx[i])

sum_W_sx = sum(W_sx.values())
P_sx = {}
for key in W_sx.keys():
    P_sx[key] = W_sx[key]/sum_W_sx
for i in P_sx:
    print(i, ":", P_sx[i])

sum_W_xe = sum(W_xe.values())
P_xe = {}
for key in W_xe.keys():
    P_xe[key] = W_xe[key]/sum_W_xe
for i in P_xe:
    print(i, ":", P_xe[i])
W_new = {}
W_new["sA"] = W[0][1]+1-P_sx["sA"]
W_new["sV"] = W[0][2]+1-P_sx["sV"]
W_new["sN"] = W[0][3]+1-P_sx["sN"]
W_new["AN"] = W[1][3]+1-P_xx["AN"]
W_new["AV"] = W[1][2]+1-P_xx["AV"]
W_new["VN"] = W[2][3]+1-P_xx["VN"]
W_new["VV"] = W[2][2]+1-P_xx["VV"]
W_new["NN"] = W[3][3]+1-P_xx["NN"]
W_new["NV"] = W[3][2]+1-P_xx["NV"]
W_new["Ne"] = W[3][4]+1-P_xe["Ne"]
W_new["Ve"] = W[2][4]+1-P_xe["Ve"]

for i in W_new:
    print(i, ":", W_new[i])

