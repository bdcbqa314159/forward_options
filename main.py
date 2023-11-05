# pylint: disable-all

import numpy as np
from scipy.stats import norm

def d_1(F_t, K, sigma, t, T):
    B = sigma*np.sqrt(T-t)
    A = np.log(F_t/K)/B + 0.5*B
    return A

def d_2(F_t, K, sigma, t, T):
    return d_1(F_t, K, sigma, t, T) - sigma*np.sqrt(T-t)

def discount(r,t,T):
    return np.exp(-r*(T-t))

def N(x):
    return norm.cdf(x)

def forward(S_t, r, t, T):
    P_t_T = 1/discount(r,t,T)
    G_t = S_t/P_t_T
    return G_t

def call(S_t, S_0, r, sigma, t, T):

    G_t = forward(S_t, r, t, T)
    G_0 = forward(S_0, r, 0, T)

    d_1 = d_1(G_t, G_0, sigma, t, T)
    d_2 = d_2(G_t, G_0, sigma, t, T)
    return discount(r,t,T)*(G_t*N(d_1) - G_0*N(d_2))

def put(S_t, S_0, r, sigma, t, T):

    G_t = forward(S_t, r, t, T)
    G_0 = forward(S_0, r, 0, T)

    d_1 = d_1(G_t, G_0, sigma, t, T)
    d_2 = d_2(G_t, G_0, sigma, t, T)
    return discount(r,t,T)*(-G_t*N(-d_1) + G_0*N(-d_2))

if __name__ == '__main__':
    print('forward options')