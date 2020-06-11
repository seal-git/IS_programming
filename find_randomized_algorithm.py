'''
Created on 2020/06/10

@author: seal0
'''
import numpy as np

def calc_pr_and_e():
    #prがTrue => aは乱択n-近似アルゴリズム
    #eがTrue => aは乱択n-平均近似アルゴリズム
    n = 3
    a = np.random.randint(1, 10, n)
    d = np.random.randint(10)
    count = 0
    for i in a:
        if(i <= d):
            count+=1

    if(count/n > 0.5):
        pr = True
    else:
        pr = False

    if(sum(a)/n<d):
        e = True
    else:
        e = False

    if(pr==False and e==True):
        print("d=", d, "\n", "a=", a)
        print("count=", count,"pr=", count/n)
        print("e=", sum(a)/n)


if __name__ == '__main__':
    pass

for i in range(100):
    calc_pr_and_e()



