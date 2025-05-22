# Aggressive Cows

# Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.


# Examples:
# Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]

# Output: 3

# Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

# Input : n = 5, k = 2, nums = [4, 2, 1, 3, 6]

# Output: 5

# Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions [1, 6]. 


def can_place_cows(stalls, k , min_dist):
    count = 1
    last_pos = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= min_dist:
            count += 1
            last_pos = stalls[i]
        
        if count == k:
            return True
    return False

def aggressive_cows(n, k , nums):
    nums.sort()
    
    low = 1
    high = nums[-1] - nums[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(nums, k , mid):
            ans = mid
            low = mid + 1
            
        else: 
            high = mid - 1
            
    return ans