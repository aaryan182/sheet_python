# leetcode 51

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def isSafe(row, col, diagnols, anti_diagnols, cols):
            return col not in cols and (row - col) not in diagnols and (row + col) not in anti_diagnols
        
        def backtrack(row, diagnols, anti_diagnols, cols):
            if row == n:
                res.append(["".join(r) for r in board])
                return 
        
            for col in range(n):
                if isSafe(row, col, diagnols, anti_diagnols, cols):
                    board[row][col] = "Q"
                    cols.add(col)
                    diagnols.add(row - col)
                    anti_diagnols.add(row + col)

                    backtrack(row + 1 , diagnols, anti_diagnols, cols)

                    board[row][col] = "."
                    cols.remove(col)
                    diagnols.remove(row - col)
                    anti_diagnols.remove(row + col)

        backtrack(0, set(), set(), set())
        return res