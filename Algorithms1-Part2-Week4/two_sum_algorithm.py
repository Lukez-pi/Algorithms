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
    lower_range = -10000
    upper_range = 10000
    
    numbers = file_processing(file_name)
    print("done processing the input file")
    
    numbers.sort()
    min_counter = 0
    max_counter = len(numbers) - 1
    sums = set()
    
    start_time = time.time()
    while min_counter < max_counter:
        if numbers[min_counter] + numbers[max_counter] < lower_range:
            min_counter += 1
        elif numbers[min_counter] + numbers[max_counter] > upper_range:
            max_counter -= 1
        else:
            for i in range(max_counter, min_counter - 1, -1):
                two_sum = numbers[min_counter] + numbers[i]
                if two_sum < lower_range:
                    break
                else:
                    sums.add(numbers[min_counter] + numbers[i])
            min_counter += 1
    print("done using a loop")
    print(time.time() - start_time)
    return len(sums)

# print(alg("2sum.txt"))