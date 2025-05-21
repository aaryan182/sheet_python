# Rat in a Maze

# Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1).

# Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).

# The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.

# Examples:
# Input : n = 4 , grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]

# Output : [ "DDRDRR" , "DRDDRR" ]

# Explanation : The rat has two different path to reach (3, 3).

# The first path is (0, 0) => (1, 0) => (2, 0) => (2, 1) => (3, 1) => (3, 2) => (3, 3).

# The second path is (0,0) => (1,0) => (1,1) => (2,1) => (3,1) => (3,2) => (3,3).

# Input : n = 2 , grid = [ [1, 0] , [1, 0] ]

# Output : -1


def is_safe(x, y, grid, visited, n):
    return 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and not visited[x][y]

def solve(x, y, path, grid, visited, n, result):
    if x == n - 1 and y == n - 1:
        result.append(path)
        return 
    
    directions = [('D', 1, 0), ('L', 0 , -1), ('R', 0, 1), ('U', -1, 0)]
    
    for dir_char, dx, dy, in directions:
        new_x, new_y = x + dx, y + dy
        if is_safe(new_x, new_y, grid , visited, n):
            visited[x][y] = True
            solve(new_x, new_y, path + dir_char, grid, visited, n, result)
            visited[x][y] = False
            
def findPath(grid, n):
    if grid[0][0] == 0:
        return [-1]
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = []
    solve(0, 0, "", grid, visited, n, result)
    return sorted(result) if result else [-1]