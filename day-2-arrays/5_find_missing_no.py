# Find the repeating and missing number

# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.


# Examples:
# Input: nums = [3, 5, 4, 1, 1]

# Output: [1, 2]

# Explanation: 1 appears two times in the array and 2 is missing from nums

# Input: nums = [1, 2, 3, 6, 7, 5, 7]

# Output: [7, 4]

# Explanation: 7 appears two times in the array and 4 is missing from nums.


def findErrorNums(nums):
    n = len(nums)
    sum_n = n * (n + 1) // 2
    sum_sq_n = n * (n + 1) * (2 * n + 1) // 6
    
    sum_nums = sum(nums)
    sum_sq_nums = sum(x *x for x in nums)
    
    diff = sum_nums - sum_n
    sq_diff = sum_sq_nums - sum_sq_nums
    
    sum_ab = sq_diff // diff
    
    A = (diff + sum_ab) // 2
    B = A - diff
    
    return [A, B]
    