# Print Shortest Path - Dijkstra’s Algorithm

# Problem Statement: 

# You are given a weighted undirected graph having n+1 vertices numbered from 0 to n and m edges describing there are edges between a to b with some weight, find the shortest path between the vertex 1 and the vertex n, and if the path does not exist then return a list consisting of only -1.

# Note: Please read the G-32 and the G-33 article before reading this article to get a clear understanding of Dijkstra’s Algorithm will form the base for this particular problem.

# Examples: 

# Example 1:

# Input:
# n = 5, m= 6
# edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
# Output:
# 1 4 3 5
# Explanation: 
# The source vertex is 1. Hence, the shortest distance path 
# of node 5 from the source will be 1->4->3->5 as this is 
# the path with a minimum sum of edge weights from source 
# to destination.

import heapq
from collections import defaultdict


class Solution:
    def shortestPath(self, n, m, edges):
        graph = defaultdict(list)
        for u, v, wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))
            
        dist = [float('inf')] * (n + 1)
        parent = [i for i in range(n + 1)]
        
        min_heap  = [(0,1)]
        dist[1] = 0
        
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)
            
            for v , wt in graph[u]:
                if curr_dist + wt < dist[v]:
                    dist[v] = curr_dist + wt
                    parent[v] = u
                    heapq.heappush(min_heap, (dist[v], v))
            
        if dist[n] == float('inf'):
            return [-1]

        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        return path[::-1]