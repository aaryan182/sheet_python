# Traversal Techniques
# Given an undirected connected graph with V vertices numbered from 0 to V-1, the task is to implement both Depth First Search (DFS) and Breadth First Search (BFS) traversals starting from the 0th vertex. The graph is represented using an adjacency list where adj[i] contains a list of vertices connected to vertex i. Visit nodes in the order they appear in the adjacency list.


# Examples:

# Input: V = 5, adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

# Output:[0, 2, 4, 3, 1], [0, 2, 3, 1, 4]

# Explanation:

# DFS: Start from vertex 0. Visit vertex 2, then vertex 4, backtrack to vertex 0, then visit vertex 3, and finally vertex 1. The traversal is 0 → 2 → 4 → 3 → 1.

# BFS: Start from vertex 0. Visit vertices 2, 3, and 1 (in the order they appear in the adjacency list). Then, visit vertex 4 from vertex 2. The traversal is 0 → 2 → 3 → 1 → 4.

from collections import deque

def bfs_traversal(V, adj):
    visited = [False] * V
    result = []
    queue = deque()
    
    queue.append(0)
    visited[0] = True
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    return result