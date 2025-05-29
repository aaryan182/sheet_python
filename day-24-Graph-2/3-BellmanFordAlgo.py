# Bellman Ford Algorithm

# Problem Statement: Given a weighted, directed and connected graph of V vertices and E edges, Find the shortest distance of all the vertices from the source vertex S.

# Note: If the Graph contains a negative cycle then return an array consisting of only -1.

# Example 1:

# Input Format: 
# V = 6, 
# E = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], 
# S = 0


# Result: 0 5 3 3 1 2
# Explanation: Shortest distance of all nodes from the source node is returned.


class Solution:
    def bellmanFord(self, V, edges, S):
        dist = [float('inf')] * V
        dist[S] = 0
        
        for _ in range(V-1):
            for u, v, wt in edges:
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return [-1]
        
        return dist