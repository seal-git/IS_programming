'''
Created on 2020/05/14

@author: seal0
'''

import numpy as np
from numpy import linalg as LA

A=np.array([[1.0, 1.0], [1.0, 1.01]])

print(LA.cond(A))

a=1.0
b=-4.0201
c=0.0001

ans1 = (-b+np.sqrt((b*b-4.0*a*c)))/2.0
ans2 = (-b-np.sqrt((b*b-4.0*a*c)))/2.0

print(-b/2.0)
print(np.sqrt((b*b-4.0*a*c))/2.0)
print(np.sqrt(ans1/ans2))

'''
402.00751248429464
2.01005
2.010025124842971
402.00751248408204
'''