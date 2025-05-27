# leetcode 151

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = n - 1
        result = []

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break
            
            end = i
            while i >= 0 and s[i] != ' ':
                i -= 1
            start = i + 1

            result.append(s[start:end + 1])
        
        return " ".join(result)