# leetcode 72

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            
            insert_op = 1 + dp(i, j+1)
            delete_op = 1 + dp(i+1, j)
            replace_op = 1 + dp(i+1, j + 1)

            return min(insert_op, delete_op, replace_op)
        
        return dp(0,0)