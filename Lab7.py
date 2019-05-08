# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:33:57 2019

@author: aarel
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import queue

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def breadth_first_search(G, v):
    visited = np.arange(len(G)) * False
    prev = np.arange(len(G)) * -1    
    Q = []
    Q.enqueue(v)
    while len(Q)>= 1:
        u = Q.pop()
        for t in range(len(G[u])):
           if visited[t] != True:
               visited[t] == True
               prev[t] = u
               Q.enqueue(t)
    return prev

def depth_first_search(G,source):
    visited = np.arange(len(G)) * False
    visited[source] = True
    for t in G[source]:
        if visited[t] != True:
            prev[t] = source    
    return prev 

def depth_first_search_r(G,source):
    visited = np.arange(len(G)) * False
    visited[source] = True
    for t in G[source]:
        if visited[t] != True:
            prev[t] = source
            depth_first_search(G,t)

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: 
        S[rj] = ri

def find_c(S,i):
    if S[i]<0:
        return i
    else:
        r = find_c(S,S[i])
        S[i] = r
        return r
    
def union_by_size(S,i,j):
    ri = find_c(S,i)
    rj = find_c(S,j)
    if ri != rj:
       if S[ri] > S[rj]:
           S[rj] += S[ri]
           S[rj] = rj
    else:
        S[ri] += S[rj]
        S[rj] = ri


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 


maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)
print(walls)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
remove= input("How many walls would you like to remove")

if int(remove) > len(walls):
    print("There is at least 1 path from your source to your destination")
if int(remove) < len(walls):
    print("There is not a path from source to destination guaranteed")
if int(remove) == len(walls):
    print("There is a unique path from source to destination")

S = DisjointSetForest(len(walls))
num_sets = len(S)
while num_sets>1:
    d = random.randint(0,len(walls)-1)
    print('removing wall ',walls[d])
    walls.pop(d)
    num_sets = num_sets-1
draw_maze(walls,maze_rows,maze_cols)