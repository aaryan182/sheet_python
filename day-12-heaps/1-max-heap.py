# Max heap implementation 

# A max heap is a binary tree where:
# Every parent node is greater than or equal to its child nodes.
# The largest element is always at the root.
# It is a complete binary tree, meaning all levels are completely filled except possibly the last level, which is filled from left to right.


# BRUTE FORCE APPROACH

class BruteForceMaxHeap:
    def __init__(self) -> None:
        self.heap = []
        
    def insert(self, val):
        self.heap.append(val)
        
    def extract_max(self):
        if not self.heap:
            return None
        max_val = max(self.heap)
        self.heap.remove(max_val)
        return max_val
    
    def peek(self):
        return max(self.heap) if self.heap else None
    
    

# Better approach - Heapq with negation

# Python has heapq library but it only supports min heaps
# we can insert negative values to simulate a max heap

import heapq

class MaxHeapWithHeapq:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self, val):
        heapq.heappush(self.heap, -val)
    
    def extract_max(self):
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)
    
    def peek(self):
        return -self.heap[0] if self.heap else None

