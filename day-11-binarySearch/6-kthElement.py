# Kth element of 2 sorted arrays

# Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.


# Examples:
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5

# Output: 6

# Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

# Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7

# Output: 256

# Explanation: Final sorted array is - [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892], 7th element of this array is 256.

def kthElement(a, b, k):
    if len(a)> len(b):
        return kthElement(b, a, k)
    
    low = max(0, k - len(b))
    high = min(k , len(a))
    
    while low <= high:
        cutA = (low + high) // 2
        cutB = k - cutA
        
        l1 = float('-inf') if cutA == 0 else a[cutA - 1]
        l2 = float('-inf') if cutB == 0 else b[cutB - 1]
        r1 = float('inf') if cutA == len(a) else a[cutA]
        r2 = float('inf') if cutB == len(b) else b[cutB]
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cutA - 1
        else:
            low = cutA + 1