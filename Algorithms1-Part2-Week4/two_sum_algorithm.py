# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:19:14 2020

@author: lukez
"""

#python "test set/tester/python3/tester.py" "Algorithms1-Part2-Week4\\two_sum_algorithm.py" "test set/testCases/course2/assignment2Dijkstra"

import time

def file_processing(file_name):
    numbers = []
    f = open(file_name)
    line = f.readline()
    while line:
        numbers.append(int(line))
        line = f.readline()
    f.close()
    return numbers

def alg(file_name):
    numbers = file_processing(file_name)
    numbers.sort()
    numbers_set = set(numbers)
    numbers_processed = set()
    print("done processing the input file")
    sums = set()
    lower_range = -10000
    upper_range = 10000
    t_set = set([i for i in range(lower_range, upper_range)])
    start_time = time.time()
    for idx, n in enumerate(numbers):
        temp = set()
        if n in numbers_processed:
            continue
        else:
            numbers_processed.add(n)
            if idx % 1000 == 0:
                print("size of t: {}".format(len(t_set)))
                print("currently at generation {}".format(idx))
                print("it has taken {} s".format(start_time - time.time()))
            for t in t_set:
                if t - n in numbers: # to satisfy the x + y = t condition (x, y both from the numbers set)
                    sums.add(t)
                    temp.add(t)
        t_set = t_set - temp
    return len(sums)

print(alg("2sum.txt"))