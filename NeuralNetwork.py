'''
Created on 2020/07/07

@author: tohoseal
'''
import numpy as np


def 活性化(z):
    return(np.tanh(z))

def back活性化(前):
    return(1/np.square(np.cosh(前)))


def 全結合(W,X):
    z = np.dot(W,X)
    return z

def 損失関数(正解,出力):
    return(np.square(正解-出力)/2)

def back損失関数(正解, 出力):
    return(正解-出力)

def 行列積(A,B,C):
    AB = np.dot(A,B)
    ABC = np.dot(AB,C)
    return(ABC)

def エポック(入力,正解):
    global 層1の重み
    global 層2の重み

    バイアス付き入力 = np.append(入力, np.array([[1]]),axis=1)
    層1の出力 = 全結合(層1の重み,バイアス付き入力.T)
    層1の微分 = 入力.T
    バイアス1の微分 = np.array([[1]])
    活性化された層1の出力 = 活性化(層1の出力)
    活性化された層1の微分 = back活性化(層1の出力)
    print("層1の出力",活性化された層1の出力)

    バイアス付き層1の出力 = np.append(活性化された層1の出力,np.array([[1]]),axis=0)

    層2の出力 = 全結合(層2の重み,バイアス付き層1の出力)
    層2の微分 = 層1の出力
    バイアス2の微分 = np.array([[1]])
    活性化された層2の出力 = 活性化(層2の出力)
    活性化された層2の微分 = back活性化(層2の出力)

    誤差 = abs(活性化された層2の出力-正解)
    print("層2の出力",活性化された層2の出力)
    print("誤差",誤差)
    if 誤差<0.001:
        return 誤差

    dLd出力 = back損失関数(正解,活性化された層2の出力)

    # print(dLd出力)
    # print(活性化された層2の微分)
    # print(層2の微分)

    dLd層2の重み = 行列積(dLd出力,活性化された層2の微分,層2の微分.T)
    dLdバイアス2の重み = 行列積(dLd出力,活性化された層2の微分,バイアス2の微分.T)

    print(dLd層2の重み)
    print(dLdバイアス2の重み)
    層2更新 = np.append(dLd層2の重み,dLdバイアス2の重み,axis=1)

    層2の重み = 層2の重み+学習率*層2更新

    print("更新した層2の重み:[[w21],[w22],[w23]]",層2の重み)

#     print(活性化された層1の微分)
#     print(層1の微分)

    dLd層1の重み = 行列積(dLd層2の重み,活性化された層1の微分,層1の微分.T)
    dLdバイアス1の重み = 行列積(dLd層2の重み,活性化された層1の微分,バイアス1の微分.T)
#     print(dLd層1の重み)

    層1更新 = np.append(dLd層1の重み,dLdバイアス1の重み,axis=1)
    層1の重み = 層1の重み+学習率*層1更新

    print("更新した層1の重み:[[w11,w13,w15],[w12,w14,w16]]",層1の重み)

    return 誤差


if __name__ == '__main__':
    pass

b = np.array([4, 9, 2])
学習率= 1.0

入力 = np.empty((1,2), dtype="float")
入力[0][0] = 1
入力[0][1] = 0

正解 = np.empty((1,1), dtype="float")

正解[0][0] = -1

層1の重み = np.empty((2,3), dtype="float")
層2の重み = np.empty((1,3), dtype="float")

層1の重み[0][0] = (b[1]+1)/10
層1の重み[1][0] = -(b[2]+1)/10
層1の重み[0][1] = (b[0]+1)/10
層1の重み[1][1] = (b[0]+1)/10
層1の重み[0][2] = (b[1]+1)/10
層1の重み[1][2] = -(b[2]+1)/10

層2の重み[0][0] = -(b[0]+1)/10
層2の重み[0][1] = -(b[1]+1)/10
層2の重み[0][2] = -(b[2]+1)/10

print("層1の重み:[[w11,w13,w15],[w12,w14,w16]]")
print(層1の重み)

print("層2の重み:[[w21],[w22],[w23]]")
print(層2の重み)

誤差 = 100

エポック(入力,正解)
# エポック(入力,正解)

# while 誤差>0.003:
#     誤差 = エポック(入力,正解)


