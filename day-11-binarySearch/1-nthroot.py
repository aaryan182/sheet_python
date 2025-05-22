# Find Nth root of a number

# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.


# Examples:
# Input: N = 3, M = 27

# Output: 3

# Explanation: The cube root of 27 is equal to 3.

# Input: N = 4, M = 69

# Output:-1

# Explanation: The 4th root of 69 does not exist. So, the answer is -1.

def power(mid, n , m):
    result = 1
    for _ in range(n):
        result *= mid
        if result > m:
            return 2
    if result == m:
        return 1
    return 0

def nth_root(N,M):
    low = 1
    high = M
    while low <= high:
        mid = (low + high) // 2
        result = power(mid, N, M)
        if result == 1:
            return mid
        elif result == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1