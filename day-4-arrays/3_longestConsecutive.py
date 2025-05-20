# leetcode 128

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_sum = num
                streak = 1

                while current_sum + 1 in num_set:
                    current_sum += 1
                    streak += 1

                longest = max(longest, streak)
        
        return longest