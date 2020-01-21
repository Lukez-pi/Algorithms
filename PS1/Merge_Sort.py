# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:48:51 2019

@author: lukez
"""
from math import ceil
# import numpy as np

def merge_sort(arr):
    if len(arr) == 1:
        return 0, arr
    
    m = ceil(len(arr) / 2)
    arr_left = arr[:m]
    arr_right = arr[m:]
    len_left = len(arr_left)
    len_right = len(arr_right)
    tot_len = len_left + len_right
    
    inversion_left, arr_left_sorted = merge_sort(arr_left)
    inversion_right, arr_right_sorted = merge_sort(arr_right)
    
    arr_sorted = []
    inversion_cross = 0
    idx_left = 0
    idx_right = 0
    
    for k in range(tot_len):
        if arr_left_sorted[idx_left] < arr_right_sorted[idx_right]:
            arr_sorted.append(arr_left_sorted[idx_left])
            idx_left += 1
        else:
            arr_sorted.append(arr_right_sorted[idx_right])
            idx_right += 1
            inversion_cross += len_left - idx_left
        
        if idx_left == len_left:
            for i in range(idx_right, len_right):
                arr_sorted.append(arr_right_sorted[i])
            break
        
        if idx_right == len_right:
            for i in range(idx_left, len_left):
                arr_sorted.append(arr_left_sorted[i])
            break
    
    inversion_tot = inversion_left + inversion_right + inversion_cross 
    return inversion_tot, arr_sorted
           
f = open("IntegerArray.txt", "r")
dataset = []
for line in f:
    dataset.append(int(line))

print(len(dataset))
inversion_tot, arr_sorted = merge_sort(dataset) #[3, 20, 700, 27, 46, 4,  9, 90000, 7]
# print(arr_sorted)
print(inversion_tot)