# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def CalculateFactorial(n):
    if n == 0:
        return 1
    else:
        return CalculateFactorial(n - 1) * n

for i in range(20):
    fac = CalculateFactorial(i)
    print('The factorial of {} is {}'.format(i, fac))