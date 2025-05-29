# Prim's Algorithm - Minimum Spanning Tree 
# Problem Statement: Given a weighted, undirected, and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
# (Sometimes it may be asked to find the MST as well, where in the MST the edge-informations will be stored in the form {u, v}(u = starting node, v = ending node).)

# Example 1:

# Input Format: 
# V = 5, edges = { {0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {4, 2, 7}}


# Result: 16
# Explanation: 
# The minimum spanning tree for the given graph is drawn below:
# MST = {(0, 1), (0, 3), (1, 2), (1, 4)}

import heapq
from collections import defaultdict

class Solution:
    def primMST(self, V: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v , wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))
        
        visited = [False] * V
        min_heap = [(0,0)]
        mst_weight = 0
        
        while min_heap:
            wt, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            
            visited[u] = True
            mst_weight += wt
            
            for v, weight in graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))
        
        if not all(visited):
            return -1
        
        return mst_weight