# leetcode 139

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            for word in word_set:
                if i >= len(word) and s[i - len(word):i] == word:
                    if dp[i - len(word)]:
                        dp[i] = True
                        break
        
        return dp[n]