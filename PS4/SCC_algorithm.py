# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:13:21 2019

@author: lukez
"""
import sys
sys.setrecursionlimit(2 ** 30)

# =============================================================================
# for line in scc_file:
#     line = line.strip().split()
#     if len(line) != 0:
#         if line[1] in G_rev:
#             G_rev[line[1]].append(int(line[0]))
#         else:
#             G_rev[line[1]] = [int(line[0])]
#             
#         if line[0] in G: # checking if it's already a key in the dictionary
#             G[line[0]].append(int(line[1]))
#         else:
#             G[line[0]] = [int(line[1])]   
# =============================================================================

def main(filename):
    
    G = dict()
    G_rev = dict()
    check_list = dict()
    ordered_list = []
    SCC_list = []

    scc_file = open(filename, 'r')
    for line in scc_file:
        line = line.strip().split()
        if len(line) != 0:
            if line[1] in G_rev:
                G_rev[line[1]].append(int(line[0]))
            else:
                G_rev[line[1]] = [int(line[0])]
                
            if line[0] in G: # checking if it's already a key in the dictionary
                G[line[0]].append(int(line[1]))
            else:
                G[line[0]] = [int(line[1])]   

    vertex_num = 0
    for key in G_rev:
        check_list[key] = False
        vertex_num += 1
    
    for vertex_rev in G_rev:
        if vertex_rev in check_list and check_list[vertex_rev] == False:
            check_list[vertex_rev] = True
            DFS_rev(G_rev, vertex_rev, check_list, ordered_list)
    ordered_list.reverse()

    for key in check_list: # reset the keys
        check_list[key] = False
    
    for vertex in ordered_list:
        scc_size = 0
        if vertex in check_list and check_list[vertex] == False: # vertex haven't been examined yet
            scc_size = DFS(G, vertex, scc_size, check_list)
            SCC_list.append(scc_size)
        if key not in check_list:
            check_list[key] = True     
    
    SCC_list.sort(reverse = True)
    while len(SCC_list) < 5:
        SCC_list.append(0)
    
    if len(SCC_list) > 5:
        SCC_list = SCC_list[:5]
    
    print(SCC_list)
    
    str_ans = ""
    for SCC_size in SCC_list:
        str_ans += str(SCC_size)
        str_ans += ','
    str_ans = str_ans[:-1]
    return str_ans

def DFS_rev(G_rev, node, check_list, ordered_list):
    check_list[node] = True
    edge_num = len(G_rev[node]) # do not include the vertex itself
    for i in range(edge_num):
        head_vertex = G_rev[node][i]
        # print(node + " -> " + str(head_vertex))
        key = str(head_vertex)
        if key in check_list and check_list[key] == False:
            DFS_rev(G_rev, str(head_vertex), check_list, ordered_list)
        if key not in check_list: # meaning reached a deadend
            check_list[key] = True 
            ordered_list.append(key)
    ordered_list.append(node)
    
def DFS(G, node, scc_size, check_list):
    check_list[node] = True
    scc_size += 1
    if node not in G:
        return scc_size
    
    edge_num = len(G[node]) # do not include the vertex itself
    for i in range(edge_num):
        head_vertex = G[node][i]
        key = str(head_vertex)
        if key in check_list and check_list[key] == False:
            # check_list[key] = True # set the vertex to being checked
            scc_size = DFS(G, str(head_vertex), scc_size, check_list)
        if key not in check_list:
            check_list[key] = True
            scc_size += 1
    return scc_size

if __name__ == "__main__":
    str_ans = main()
    print(str_ans)