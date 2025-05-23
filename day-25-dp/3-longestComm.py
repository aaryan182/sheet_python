# leetcode 1143

from functools import lru_cache

# Tabulation approach DP ( bottom up)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i+1, j), dp(i, j+1))
        
        return dp(0,0)
    
    
# Memoization approach Dp ( top down)

def longestCommonSubsequence(text1, text2):
    @lru_cache(None)
    def dp(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + dp(i + 1, j + 1)
        else:
            return max(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)