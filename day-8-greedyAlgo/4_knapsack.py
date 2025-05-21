# Fractional Knapsack Problem : Greedy Approach

# Problem Statement: The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.

# Note: We can either take the item as a whole or break it into smaller units.

# Example:

# Input: N = 3, W = 50, values[] = {100,60,120}, weight[] = {20,10,30}.

# Output: 240.00

# Explanation: The first and second items  are taken as a whole  while only 20 units of the third item is taken. Total value = 100 + 60 + 80 = 240.00

def fractinal_knapsack(values, weights, W):
    n = len(values)
    
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(n)]
    
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    reamining_capacity = W
    
    for value , weight , ration in items:
        if reamining_capacity == 0:
            break
        
        if weight <= reamining_capacity:
            total_value += value
            reamining_capacity -= weight
        
        else:
            total_value += ration * reamining_capacity
            reamining_capacity = 0
        
    return round(total_value, 2)