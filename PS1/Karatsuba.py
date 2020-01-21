# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:50:58 2019

@author: lukez
"""

from math import log, ceil

x = 5678
y = 1234

def karatsuba_multiplication(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n1 = ceil(log(x, 10)) # n is the total number of digits
    n2 = ceil(log(y, 10))
    n = min(n1, n2);
    m = ceil(n / 2) # m is the number of digits for the right half of the number
    
    div = 10 ** m
    a = x // div
    b = x % div
    # print('a = {}, b = {}'.format(a, b))
    
    c = y // div
    d = y % div
    # print('c = {}, d = {}'.format(c, d))
    
    a_c = karatsuba_multiplication(a, c)
    b_d = karatsuba_multiplication(b, d)
    a_b_c_d = karatsuba_multiplication(a + b, c + d) # (a + b) * (c + d)
    ad_bc = a_b_c_d - a_c - b_d
    return (10 ** (m * 2)) * a_c + (10 ** m) * ad_bc + b_d

product = karatsuba_multiplication(102443, 90058989)
print(product)