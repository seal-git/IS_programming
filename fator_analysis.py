'''
Created on 2020/06/04

@author: seal0
'''
import numpy as np
import math

if __name__ == '__main__':
    pass

#data samples
n =[4,9,2,1]
X = np.array([[n[2]+n[3], n[0]], [n[3],n[1]+n[3]],[n[1],n[0]+n[3]], [n[0]+n[1],n[2]],[n[1]+n[2],n[0]+n[2]]], dtype="float")
print(X)
mean = np.empty([2])
mean[0] = sum(X[:, 0])/5.0
mean[1] = sum(X[:, 1])/5.0

I = 1
W = np.array([1,0])
mu = np.array([0,0])
sigma = np.array([[1,0],[0,1]])
print("X=", X)
print("mean=", mean)

#calculate X'_ij = X_ij - mean[j]
XX = X
for i in range(5):
    for j in range(2):
        XX[i][j]=X[i][j]-mean[j]
print("XX=",XX)

#calculate sigma^(z|x) = (W^T sigma^(-1) W + I)^(-1)
sigma_z_x = 1/(np.dot(np.dot(W.T,np.linalg.inv(sigma)), W)+I)

#calculate mu_i^(z|x) = sigma^(z|x) W^T sigma^(-1) X'[i]
mu_z_x = np.empty([5])
for i in range(5):
    mu_z_x[i] = np.dot(np.dot(W.T * sigma_z_x, np.linalg.inv(sigma)), XX[i])

print("sigma_z_x=", sigma_z_x)
print("mu_z_x=", mu_z_x)

#calculate <ZZ^T>_i = sigma^(z|x) + mu_i^(z|x) (mu_i^(z|x))^T
ZZ = np.array([sigma_z_x + mu_z_x[i]**2 for i in range(5)])
print("ZZ=", ZZ)


# calculate sufficient statistics
XX_sum = np.diag(np.diag(sum([np.dot(XX[i][:, None], XX[i][None, :]) for i in range(5)])))
ZZ_sum = sum(ZZ)
XZ_sum = sum(XX[i] * ZZ[i] for i in range(5))

print("XX_sum=", XX_sum)
print("ZZ_sum=", ZZ_sum)
print("XZ_sum=", XZ_sum)

#update W and sigma
W_next = XZ_sum / ZZ_sum
sigma_next = np.diag(np.diag(XX_sum - np.dot(XZ_sum, W_next.T)))/5

print("W_next=", W_next)
print("sigma_next=", sigma_next)

#calculate p(x|lambda)
sigma_before = np.dot(W[:,None], W.T[None,:])+sigma
sigma_after = np.dot(W_next, W_next.T)+sigma_next

print("sigma_before=", sigma_before)
print("sigma_after=", sigma_after)





