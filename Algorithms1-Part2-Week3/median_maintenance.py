# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:18:14 2020

@author: lukez
"""
import math

def file_processing(file_name):
    stream = []
    f = open(file_name)
    line = f.readline()
    while line:
        stream.append(int(line))
        line = f.readline()
    f.close()
    return stream

class heap():
    def __init__(self, is_pair, is_max_heap):
        self.heap = []
        self.is_pair = is_pair
        self.is_max_heap = is_max_heap
        self.position_tracker = dict()
        
    def insert(self, v):
        def swap_helper(pos, parent_pos, parent):
            self.heap[pos] = parent
            self.heap[parent_pos] = v
            if self.is_pair:
                self.position_tracker[parent[1]] = pos
                self.position_tracker[v[1]] = parent_pos
            pos = parent_pos
            return pos                
        
        self.heap.append(v)
        pos = len(self.heap) - 1
        if self.is_pair:
            self.position_tracker[v[1]] = pos
        
        while pos != 0:
            parent_pos = math.ceil(pos / 2) - 1
            parent = self.heap[parent_pos]
            if self.is_max_heap:
                if parent < v:
                    pos = swap_helper(pos, parent_pos, parent)
                else:
                    break
            else:    
                if parent > v:
                    pos = swap_helper(pos, parent_pos, parent)
                else:
                    break
    
    def extract(self):
        pos = 0
        first_val = self.heap[0]
        v = self.heap.pop() # default behavior is to remove the last element
        if self.is_pair:
            self.position_tracker[v[1]] = pos
            del self.position_tracker[first_val[1]]
        if len(self.heap) != 0:
            self.heap[0] = v
            self.bubble_down(v, pos)           
        return first_val
    
    
    def del_elem(self, elem_idx):
        if self.is_pair:
            del_key = self.heap[elem_idx][1]
            del self.position_tracker[del_key]
        v = self.heap.pop()
        
        if len(self.heap) > elem_idx:    
            self.heap[elem_idx] = v
            if self.is_pair:
                self.position_tracker[v[1]] = elem_idx
                
            self.bubble_down(v, elem_idx)
        
    def bubble_down(self, v, pos):
        def swap_helper(pos, parent, parent_pos):
            parent = self.heap[parent_pos]
            self.heap[pos] = parent
            self.heap[parent_pos] = v
            if self.is_pair:
                self.position_tracker[parent[1]] = pos
                self.position_tracker[v[1]] = parent_pos
            pos = parent_pos
            return pos
        
        while (2 * pos + 1) < len(self.heap):
            parent_pos_1 = 2*pos + 1
            parent_pos_2 = 2*pos + 2
            parent_1 = self.heap[parent_pos_1]
            
            if parent_pos_2 >= len(self.heap):
                parent_pos = parent_pos_1
                parent = parent_1
            else:
                parent_2 = self.heap[parent_pos_2]
                if self.is_max_heap:
                    [parent_pos, parent] = [parent_pos_1, parent_1] if parent_1 > parent_2 else [parent_pos_2, parent_2]
                else:
                    [parent_pos, parent] = [parent_pos_1, parent_1] if parent_1 < parent_2 else [parent_pos_2, parent_2]
                    
            if self.is_max_heap:
                if v < parent:
                    pos = swap_helper(pos, parent, parent_pos)
                else:
                    break          
            else:
                if v > parent:
                    pos = swap_helper(pos, parent, parent_pos)
                else:
                    break
            
    def __repr__(self):
        return str(self.heap)


def alg(file_name):
    stream = file_processing(file_name)
    min_heap = heap(False, False)
    max_heap = heap(False, True)
    
    median_sum = 0
    for idx, val in enumerate(stream):
        min_heap_arr = min_heap.heap
        max_heap_arr = max_heap.heap
        if len(min_heap_arr) == len(max_heap_arr):
            try:
                if val < max_heap_arr[0]:
                    max_heap.insert(val)
                else:
                    min_heap.insert(val)
            except:
                min_heap.insert(val)
        elif len(min_heap_arr) > len(max_heap_arr):
            if val > min_heap_arr[0]:
                min_val = min_heap.extract()
                min_heap.insert(val)
                max_heap.insert(min_val)
            else:
                max_heap.insert(val)
        elif len(max_heap_arr) > len(min_heap_arr):
            if val < max_heap_arr[0]:
                max_val = max_heap.extract()
                max_heap.insert(val)
                min_heap.insert(max_val)
            else:
                min_heap.insert(val)
                
        if (idx + 1) % 2 == 0:
            median = max_heap_arr[0]        
        else:
            median = max_heap_arr[0] if len(max_heap_arr) > len(min_heap_arr) else min_heap_arr[0]
        median_sum += median
    return median_sum % 10000

