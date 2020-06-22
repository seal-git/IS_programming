'''
Created on 2020/06/15

@author: seal0
'''
import numpy as np
from scipy.stats import norm

if __name__ == '__main__':
    pass

b = np.array([1, 2, 9, 4], dtype="float")
x= np.array([10*i+20 for  i in b])
print(x)

A=1
W=1
Sigma = 10
Gamma = 20
mu = 200
P = 50
logp_conditional = []

for i in range(4):
    predicted_mean = A*mu #2-1, mu_{t|t-1}
    predicted_cov = A*P*A+Gamma #2-2, P_{t|t-1}
    #2-3, 2-4
    #p(z_t|x_{1:t-1})=N(z_t; predicted_mean, predicted_cov)
    print(i+2, "-1:", predicted_mean)
    print(i+2, "-2:", predicted_cov)
    print(i+2, "-3,", i+2, "-4:", predicted_mean, ",", predicted_cov)

    mean = W*predicted_mean #2-5
    cov = W*predicted_cov*W+Sigma #2-6
    logp_conditional.append(np.log(norm.pdf(x=x[i], loc=mean, scale=np.sqrt(cov)))) #2-7
    print(i+2, "-5:", mean)
    print(i+2, "-6:", cov)
    print(i+2, "-7:", logp_conditional[i])
    if i!=0:
        logp_cooccurrence = logp_conditional[i]+logp_conditional[i-1]
        print(i+2, "-8:", logp_cooccurrence)

    kalman_gain = predicted_cov*W/(W*predicted_cov*W+Sigma) #2-8
    update_mean=predicted_mean+kalman_gain*(x[i]-W*predicted_mean) #2-9
    update_cov = (1-kalman_gain*W)*predicted_cov #2-10
    #2-11, 2-12
    #p(z_t|x_t)=N(z_t; update_mean, update_cov)
    print(i+2, "-9:", kalman_gain)
    print(i+2, "-10:", update_mean)
    print(i+2, "-11:", update_cov)
    print(i+2, "-12,", i+2, "-13:", update_mean, ",", update_cov)

    mu = update_mean
    P = update_cov

