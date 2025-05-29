# leetcode 1520

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}

        for i, char_code in enumerate(map(ord, s)):
            char = chr(char_code)
            if char not in first:
                first[char] = i
            last[char] = i

        intervals = []

        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char not in first:
                continue

            start_idx = first[char]
            end_idx = last[char]

            curr_start = start_idx
            curr_end = end_idx
            
            i = curr_start
            valid_substring = True
            while i <= curr_end:
                if first[s[i]] < curr_start: 
                    valid_substring = False
                    break 
                curr_end = max(curr_end, last[s[i]])
                i += 1
            
            if valid_substring:
                intervals.append((curr_start, curr_end))

        if not intervals:
            return []

        intervals.sort(key=lambda x: (x[1], x[0]))

        result_substrings = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end: 
                result_substrings.append(s[start : end + 1])
                prev_end = end
        
        return result_substrings