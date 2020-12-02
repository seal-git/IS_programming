'''
Created on 2020/12/02

@author: tohoseal
'''
import math
import numpy as np


#誤差逆伝播法
#課題URL：https://docs.google.com/presentation/d/1o2GPLEo1P6v1zcbaHWxmIDxvrVNVsPWsBBgZqkcloW8/edit#slide=id.ga641e059a1_1_1360

def f1(x,y):
    return np.dot(x,y)
def f2(x,y):
    return x+y
def f3(x):
    return np.tanh(x)
def f4(x,y):
    return np.concatenate([x,y],axis=0)
def CE(x,y):
    return -sum(x*np.log(y))
def softmax(x):
    x_sum = sum([np.exp(x[i][0]) for i in range(3)])
    return np.array([[np.exp(x[i][0])/x_sum] for i in range(3)])
# def back_softmax(label,o6):
#     for i in range(3):
#         if(label[i][0]==1.0):
#             true = i
#             break
#     return np.array([[o6[i][0]*(1-o6[i][0])] if i==true else [-o6[i][0]*o6[true][0]] for i in range(3)])
# def back_CE(label,o6):
#     return np.array([[o6[i][0]] if label[i][0]==0.0 else [o6[i][0]-1.0] for i in range(3)])
def back_CE_softmax(label,o7):
    return o7-label
def back_f4(x):
    return np.array([[1,0,0,0],[0,1,0,0]])
def back_f3(x):
    return 1-(np.tanh(x))**2
def back_f2(b):
    return 1
def back_f1(x):
    return x.T

#初期値
H = np.array([[0.5,-1.0],[-0.2,1.0]])
x = np.array([[0.8],[-0.3]])
d = np.array([[0.1],[0.2]])
U = np.array([[0.2,-0.5,0.3,-0.1],[-0.1,0.3,0.4,0.1],[0.1,0.5,0.2,-0.2]])
b = np.array([[0.2],[-0.1],[0.1]])
label = np.array([[0.0],[1.0],[0.0]])
alpha = 0.01
i = 0
while(1):
    i+=1
    #forward
    o1 = f1(H,x)
#     print(o1)
    o2 = f2(o1,d)
#     print(o2)
    o3 = f3(o2)
#     print(o3)
    o4 = f4(o3,x)
#     print(o4)
    o5 = f1(U,o4)
    o6 = f2(o5,b)
    o7 = softmax(o6)
    l = CE(label,o7)

#     print(o5)
#     print(o6)
#     print(o7)
    print(l)
    if(i>100):
        break

    #backward
    #演算記号@は行列積、*はアダマール積を示す
    #softmaxとCEは合成すると逆伝播が簡単になる
    #back_f4,f3でかなりハマった。結局f4は上半分だけ返す、f3はアダマール積で掛けるのが正解
    u_b = b - alpha*back_CE_softmax(label,o7)*back_f2(b)
#     print(u_b)
    u_U = U - alpha*(back_CE_softmax(label,o7)*back_f2(o5)@back_f1(o4))
#     print(u_U)
    u_d = d - alpha*(back_f4(o3)@(back_f1(U)@(back_CE_softmax(label,o7)*back_f2(o5)))*back_f3(o2))
#     print(u_d)
    u_H = H - alpha*(back_f4(o3)@(back_f1(U)@(back_CE_softmax(label,o7)*back_f2(o5)))*back_f3(o2))@back_f1(x)
#     print(u_H)

    #重みの更新
    H = u_H
    d = u_d
    U = u_U
    b = u_b

    if(i==1 or i==2):
        print(o6)
        print(o7)
        print(H)
        print(d)
        print(U)
        print(b)
