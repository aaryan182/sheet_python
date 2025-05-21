# Find minimum number of coins

# Problem Statement: Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change.

# Examples:

# Example 1:

# Input: V = 70

# Output: 2

# Explaination: We need a 50 Rs note and a 20 Rs note.

# Example 2:

# Input: V = 121

# Output: 3

# Explaination: We need a 100 Rs note, a 20 Rs note and a 1 Rs coin.

def min_coins(V):
    denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    result = []
    
    for coin in denominations:
        while V >= coin:
            V -= coin
            count += 1
            result.append(coin)
    
    return count, result