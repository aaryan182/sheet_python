# Matrix chain multiplication

# Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.



# Given an array nums of size n. Dimension of matrix Ai ( 0 < i < n ) is nums[i - 1] x nums[i].Find a minimum number of multiplications needed to multiply the chain.


# Examples:
# Input : nums = [10, 15, 20, 25]

# Output : 8000

# Explanation : There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.

# If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.

# If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.

# Thus minimum number of multiplications required is 8000.

# Input : nums = [4, 2, 3]

# Output : 24

# Explanation : There is only one way to multiply the chain - A1*A2.

# Thus minimum number of multiplications required is 24.

class Solution:
    def matrixMultiplication(self, nums):
        n = len(nums)
        dp = [[ 0 for _ in range(n)] for _ in range(n)]
        
        for l in range(2,n):
            for i in range(1, n-l+1):
                j = i + l -1
                dp[i][j] = float('inf')
                for k in range(i,j):
                    cost = dp[i][k] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j]
                    dp[i][j] = min(dp[i][j], cost)
        return dp[1][n-1]