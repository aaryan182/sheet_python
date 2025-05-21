# leetcode 37

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Find all empty cells at the beginning
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
        
        # Track numbers already used in each row, column and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Populate the tracking sets
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    box_idx = (i // 3) * 3 + j // 3
                    boxes[box_idx].add(num)
        
        def backtrack(cell_idx):
            if cell_idx == len(empty_cells):
                return True
            
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + c // 3
            
            for num in map(str, range(1, 10)):
                if (num not in rows[r] and 
                    num not in cols[c] and 
                    num not in boxes[box_idx]):
                    
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    
                    # Move to next cell
                    if backtrack(cell_idx + 1):
                        return True
                    
                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            
            return False
        
        backtrack(0)