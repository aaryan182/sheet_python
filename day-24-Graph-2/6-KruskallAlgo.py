# Kruskal's Algorithm - Minimum Spanning Tree 

# Problem Statement: Given a weighted, undirected, and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

# Example 1:

# Input Format: 
# V = 5, edges = { {0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {1, 4, 5}, {4, 2, 7}}


# Result: 16
# Explanation: The minimum spanning tree for the given graph is drawn below:
# MST = {(0, 1), (0, 3), (1, 2), (1, 4)}


class DSU:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution:
    def kruskalMST(self, V: int, edges: list[list[int]]) -> int:
        edges.sort(key = lambda x: x[2])
        
        dsu = DSU(V)
        mst_weight = 0
        edges_head = 0
        
        for u , v, wt , in edges:
            if dsu.union(u,v):
                mst_weight += wt
                edges_used += 1
                if edges_used == V - 1:
                    break
                
        if edges_used != V - 1:
            return -1
        
        return mst_weight