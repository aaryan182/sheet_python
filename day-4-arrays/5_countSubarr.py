# Count subarrays with given xor K

# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.

# Examples:
# Input : nums = [4, 2, 2, 6, 4], k = 6

# Output : 4

# Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]

# Input :nums = [5, 6, 7, 8, 9], k = 5

# Output : 2

# Explanation : The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]

from collections import defaultdict

def count_subarrays_with_xor_k(nums, k):
    count = 0
    xor = 0
    freq = defaultdict(int)
    
    for num in nums:
        xor ^= num
        
        if xor == k:
            count += 1
            
        count += freq[xor ^ k] 
        
        freq[xor] += 1
    
    return count