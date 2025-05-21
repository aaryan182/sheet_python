# M Coloring Problem

# Given an integer M and an undirected graph with N vertices and E edges. The goal is to determine whether the graph can be coloured with a maximum of M colors so that no two of its adjacent vertices have the same colour applied to them.

# In this context, colouring a graph refers to giving each vertex a different colour. If the colouring of vertices is possible then return true, otherwise return false.

# Examples:
# Input : N = 4 , M = 3 , E = 5 , Edges = [ (0, 1) , (1, 2) , (2, 3) , (3, 0) , (0, 2) ]

# Output : true

# Explanation : Consider the three colors to be red, green, blue.

# We can color the vertex 0 with red, vertex 1 with blue, vertex 2 with green, vertex 3 with blue.

# In this way we can color graph using 3 colors at most.


def isSafe(node, color , graph, col , N):
    for neighbor in range(N):
        if graph[node][neighbor] == 1 and col[neighbor] == color:
            return False
    return True

def solve(node, col , graph, N, M):
    if node == N:
        return True
    for c in range(1, M +1):
        if isSafe(node, c, graph, col ,N):
            col[node] = c
            if solve(node + 1, col, graph, N, M):
                return True
            col[node] = 0
    return False

def graphColoring(graph, M, N):
    col = [0] * N 
    return solve(0, col, graph, N, M)