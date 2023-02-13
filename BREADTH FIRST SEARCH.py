#!/usr/bin/env python
# coding: utf-8

# <b>BREADTH FIRST SEARCH

# <b>REPRESENTATION OF THE GRAPH

# In[1]:


my_graph = {
    
    'S':['A','B','C'],
    'A':['S','B','D'],
    'B':['S','A','D','H'],
    'C':['S','L'],
    'D':['A','B','F'],
    'E':['G','K'],
    'F':['D','H'],
    'G':['H','E'],
    'H':['B','F','G'],
    'I':['L','K'],
    'J':['L','K'],
    'K':['I','J','E'],
    'L':['C','I','J']
    
}


# <b>IMPORT DEQUE

# In[2]:


from collections import deque


# <b>BREADTH FIRST SEARCH

# In[3]:


def bfs(graph,start,goal):
    visited = []
    queue=deque([start]) #entry point
    while queue:
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            print("Have visited: ",node)
            neighbours = graph[node]
            if node == goal :
                return("Goal is reached via path: ",visited)
            for neighbours in neighbours :
                queue.append(neighbours)
    


# <b>CASE 1 :
#     <br>START NODE : S 
#     <br>GOAL/END NODE: F

# In[4]:


bfs(my_graph,'S','F')


# <b>CASE 2:
#     <br>START NODE : S
#     <br>GOAL/END NODE: E

# In[5]:


bfs(my_graph,'S','E')


# <b>WORK DESCRIPTION OF BFS - BREADTH FIRST SEARCH

# <b>BFS - BREADTH FIRST SEARCH

# Breadth First Search (BFS) is an algorithm for traversing or searching a graph data structure or tree. It starts at the root node and explores the neighbor nodes first, before moving to the next level neighbors. BFS visits all the vertices of a graph or all the nodes of a tree at a certain depth before going deeper. It is useful for finding the shortest path between nodes in a graph and for solving problems that require searching all neighbors before visiting deeper levels. The algorithm uses a queue data structure to store the nodes that need to be visited.

# <b>ALGORITHM

# 1. Initialize a queue with the start node and mark it as visited.
# 2. Dequeue the next node from the queue and examine all its unvisited neighbors.
# 3. Enqueue the unvisited neighbors and mark them as 'have visited'.
# 4. Repeat steps 2 and 3 until either the end node is found or there are no more nodes in the queue.
# 5. The end node is found when all its neighbors have been visited, and it is added to the queue. 
# 

# <b>CODE

# 1.<b>'graph'</b> is a dictionary where each key represents a node, and its value is a set of nodes connected to it.
# <br>2. 'start' is the starting node.
# <br>3. <b>'visited'</b> is a set of visited nodes to keep track of already processed nodes.
# <br></b>4. 'queue'</b> is a deque used to keep track of the next node to visit.
# <br>5. The algorithm adds the </b>'start'</b> node to the queue and continues to process nodes until the queue is empty.
# <br>6. At each iteration, the next node is removed from the queue and added to the </b>'visited'</b> set.
# <br>7. The algorithm then adds all unvisited neighbors of the current node to the queue.
# <br>8. Finally, the <b>'visited'</b> set is returned as the result.
# 

# <b>CASE 1:</b>
# <br>start - S
# <br>end- F
# <br>BFS starts with the root node 'S' and moves to the next level neighbour A and explores that level completely i.e B and C as well.
# It then goes to the next level i.e D, H, L. This cycle is continued until the goal node F is reached.
# 

# ![bfs_f.png](attachment:bfs_f.png)

# <b>CASE 2:</b>
# <br>start - S
# <br>end- E
# <br>BFS starts with the root node 'S' and moves to the next level neighbour A and explores that level completely i.e B and C as well.
# It then goes to the next level i.e D, H, L. This cycle is continued until the goal node E is reached.

# ![bfs.png](attachment:bfs.png)
