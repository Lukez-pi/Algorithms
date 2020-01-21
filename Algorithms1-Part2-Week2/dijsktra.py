# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def file_processing():
    graph = dict()
    f = open("dijkstraData.txt")
    line = f.readline()
    while line:
        temp = line.split()
        start_v = temp[0]
        end = temp[1:]
        for e in end:
            temp_e = e.split(",")
            end_v = temp_e[0]
            dist = int(temp_e[1])
            try:
                graph[start_v][end_v] = dist
            except:
                graph[start_v] = {end_v: dist}
        line = f.readline()
    f.close()
    return graph

def dijkstra_algorithm(source_v, graph):
    X = {source_v: 0}
    max_score = 1e6
    while len(X) != len(graph): # the main loop that iterates through all vertices in the graph
        d_score_min = [max_score]
        for u in X: # scan through all vertices that has already been absorbed into X
            for end_v in graph[u]: # and look for outgoing edges where its ending point lands outside of the frontier
                if end_v not in X:
                    d_score = X[u] + graph[u][end_v] # dijsktra score = minimum distance to u + distance from u -> v
                    if d_score < d_score_min[0]:
                        d_score_min = [d_score, end_v] # update the min dijkstra score with the associated vertex
        X[d_score_min[1]] = d_score_min[0]
    return X            

def dijkstra_algorithm_heap(source_v, graph):
    X = {source_v: 0}
    max_score = 1e6
    dijkstra_heap = heap(True)
    for v in graph.keys():
        if v != source_v:
            if v in graph[source_v]:
                dijkstra_heap.insert([graph[source_v][v], v])
            else:
                dijkstra_heap.insert([max_score, v])
    
    while len(X) != len(graph):
        closest_v = dijkstra_heap.extract_min()
        dijkstra_distance = closest_v[0]
        v_name = closest_v[1]
        X[v_name] = dijkstra_distance
        for connecting_v, edge_len in graph[v_name].items(): # iterate through the vertices that are connected to the newly absorbed vertex
            if connecting_v not in X: # when the vertex hasn't been added to the X set yet
                elem_idx = dijkstra_heap.position_tracker[connecting_v]
                if connecting_v != dijkstra_heap.heap[elem_idx][1]:
                    print(connecting_v)
                    print(dijkstra_heap.heap[elem_idx][1])
                    raise Exception("wrong")
                original_dist = dijkstra_heap.heap[elem_idx][0]
                new_dist = dijkstra_distance + edge_len
                if new_dist < original_dist:
                    dijkstra_heap.del_elem(elem_idx)
                    dijkstra_heap.insert([new_dist, connecting_v])
    return X

class heap():
    def __init__(self, is_pair):
        self.heap = []
        self.is_pair = is_pair
        self.position_tracker = dict()
        
    def insert(self, v):
        self.heap.append(v)
        pos = len(self.heap) - 1
        if self.is_pair:
            self.position_tracker[v[1]] = pos
        
        while pos != 0:
            parent_pos = math.ceil(pos / 2) - 1
            parent = self.heap[parent_pos]
            if parent > v:
                self.heap[pos] = parent
                self.heap[parent_pos] = v
                if self.is_pair:
                    self.position_tracker[parent[1]] = pos
                    self.position_tracker[v[1]] = parent_pos
                pos = parent_pos                
            else:
                break
    
    def extract_min(self):
        pos = 0
        min_val = self.heap[0]
        v = self.heap.pop() # default behavior is to remove the last element
        if self.is_pair:
            self.position_tracker[v[1]] = pos
            del self.position_tracker[min_val[1]]
        if len(self.heap) != 0:
            self.heap[0] = v
            self.bubble_down(v, pos)           
        return min_val
    
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
        while (2 * pos + 1) < len(self.heap):
            parent_pos_1 = 2*pos + 1
            parent_pos_2 = 2*pos + 2
            parent_1 = self.heap[parent_pos_1]
            
            if parent_pos_2 >= len(self.heap):
                parent_pos = parent_pos_1
                parent = parent_1
            else:
                parent_2 = self.heap[parent_pos_2]
                if parent_1 < parent_2:
                    parent_pos = parent_pos_1
                    parent = parent_1
                else:
                    parent_pos = parent_pos_2
                    parent = parent_2
            if v > parent:
                parent = self.heap[parent_pos]
                self.heap[pos] = parent
                self.heap[parent_pos] = v
                if self.is_pair:
                    self.position_tracker[parent[1]] = pos
                    self.position_tracker[v[1]] = parent_pos
                pos = parent_pos
            else:
                break          
            
    def __repr__(self):
        return str(self.heap)

        
graph = file_processing()
X = dijkstra_algorithm("1", graph)
X2 = dijkstra_algorithm_heap("1", graph)

def test():
    from random import randint
    h = heap(False)
    h_size = 200
    for i in range(0, h_size):
        num = randint(1, 200)
        h.insert(num)
    for idx, e in enumerate(h.heap):
        parent_1_idx = idx * 2 + 1
        parent_2_idx = idx * 2 + 2
        if parent_1_idx >= h_size:
            print("out of range")
            break
        if parent_2_idx >= h_size:
            if e > h.heap[parent_1_idx]:
                raise Exception("wrong insertion")
            break
        print(parent_1_idx)
        if e > h.heap[parent_1_idx] or e > h.heap[parent_2_idx]:
            print(e)
            print(h.heap[parent_1_idx])
            print(h.heap[parent_2_idx])
            print(h)
            raise Exception("wrong insertion")
    
vertices = [7, 37,59,82,99,115,133,165,188,197]
print("Dijkstra with naive implementation")
for v in vertices:
    print(X[str(v)])

print("Dijkstra with heap based implementation")
for v in vertices:
    print(X2[str(v)])
            
    