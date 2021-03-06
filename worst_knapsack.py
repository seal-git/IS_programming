'''
Created on 2020/05/16

@author: seal0

Find the worst combination of 2-approximate for Knapsack
d: list of w/v. d is sorted from larger one.
w: weight of a bag
v: value of a bag
Find proper d and w under the following constraints:
    out = v1+v2+...+vh
    opt = 2 * out
To find such d and w, the biggest value must be equal to out.
'''
import numpy as np
from numpy.random import randint
import knapsack

#d: list of w/v. d is sorted from larger one.
d = [3000, 2, 1, 1, 1]
#w: weight of a bag
w = [1, 1, 3002, 1, 1]
#v: value of a bag
v = [d[i]*w[i] for i in range(5)]
#l: index of the biggest value
l = v.index(max(v))

max_weight = w[0]+w[1]+w[2]-1
out = max(v[0]+v[1], v[l])
opt, used = knapsack.solve_knapsack(w, v, max_weight)


print(d)
print(w)
print(v, l)
print("out1=%d, out2=%d"%(v[0]+v[1], v[l]))
print("b=%d opt=%d out=%d rate=%f "%(max_weight, opt, out, float(opt)/ float(out)))
print(used)
