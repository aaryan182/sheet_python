# Longest subarray with sum K

# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.


# Examples:
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15

# Output: 4

# Explanation: The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

# Input: nums = [-3, 2, 1], k=6

# Output: 0

# Explanation: There is no sub-array in the array that sums to 6. Therefore, the output is 0.


def longest_subarray_sum_k(nums,k):
    prefix_sum = 0
    max_len = 0
    sum_indices = {}
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if prefix_sum == k:
            max_len = i + 1
        
        if (prefix_sum - k) in sum_indices:
            max_len = max(max_len, i - sum_indices[prefix_sum - k])
        
        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i
        
    return max_len