# 0 and 1 Knapsack

# Given two integer arrays, val and wt, each of size N, which represent the values and weights of N items respectively, and an integer W representing the maximum capacity of a knapsack, determine the maximum value achievable by selecting a subset of the items such that the total weight of the selected items does not exceed the knapsack capacity W.

# Each item can either be picked in its entirety or not picked at all (0-1 property). The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity.


# Examples:
# Input: val = [60, 100, 120], wt = [10, 20, 30], W = 50

# Output: 220

# Explanation: Select items with weights 20 and 30 for a total value of 100 + 120 = 220.

# Input: val = [10, 40, 30, 50], wt = [5, 4, 6, 3], W = 10

# Output: 90

# Explanation: Select items with weights 4 and 3 for a total value of 40 + 50 = 90.

def knapsack_dp(val, wt, w):
    n = len(val)
    dp = [[0] * (w + 1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(w + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w] , val[i-1] + dp[i-1][w - wt[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][w]