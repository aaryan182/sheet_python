# Floyd Warshall Algorithm: 
# Problem Statement: The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.

# Do it in place.

# Example 1:

# Input Format: 
# matrix[][] = { {0, 2, -1, -1},
#         {1, 0, 3, -1},{-1, -1, 0, -1},{3, 5, 4, 0} }

# Result:
# 0 2 5 -1 
# 1 0 3 -1 
# -1 -1 0 -1 
# 3 5 4 0 
# Explanation: In this example, the final matrix 
# is storing the shortest distances. For example, matrix[i][j] is 
# storing the shortest distance from node i to j.


class Solution:
    def floyWarshall(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1 and i != j:
                    matrix[i][j] = float('inf')
                    
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1