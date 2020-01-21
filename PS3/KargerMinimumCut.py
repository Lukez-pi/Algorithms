# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:50:50 2019

@author: lukez
"""
import random
import numpy as np

file = open("kargerMinCut.txt")
vertices = []
edges = []
for line in file:
    adjacency = line.split()
    adjacency = [int(i) for i in adjacency]
    edges.append(adjacency[1:])
    vertices.append(adjacency[0])

file.close()
vertices = np.array(vertices)
edges = np.array(edges)

tot_vertices = len(vertices)
tot_edges = sum(len(arr) for arr in edges)

print(tot_vertices)
print(tot_edges)


for i in range(tot_vertices- 2):
    edge_count = 0
    vertice_count = 0;
    rand_edge = random.randint(0, tot_edges)
    for edge in edges:
        edge_count += len(edge)
        
        if edge_count > rand_edge:
            edge_idx = rand_edge - (edge_count - len(edge))
            delete_vertice = edges[vertice_count][edge_idx]
            delete_edges = edges[delete_vertice]
            for delete_edge in delete_edges:
                if delete_edge == vertices[vertice_count]: 
                    edges[vertice_count] = [edge for edge in edges[vertice_count] if edge != delete_vertice] # remove the deleted vertice entry in the merge vertice
                    merged_edges = [edge for edge in delete_edges if edge != edges[vertice_count]] # remove the entry that equals to the merged_vertice
                    edges[vertice_count].extend(merged_edges) 
                else:
                    edges[delete_edge] = [edge if edge != delete_vertice else vertices[vertice_count] for edge in edges[delete_edge]]
                    edges[delete_edge].append(vertices[vertice_count])  
            edges[delete_vertice].clear()
            tot_edges = sum(len(arr) for arr in edges)
            break
                    
        else:
            vertice_count += 1
        
    
    