# Min heap implementation

# A min heap is a special type of binary tree where:
# Every parent node is less than or equal to its child nodes.
# The smallest element is always at the root.
# It is a complete binary tree, meaning it's filled left to right at every level.


# BRUTE FORCE APPROACH
class BruteForceMinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        
    def extract_min(self):
        if not self.heap:
            return None
        min_val = min(self.heap)
        self.heap.remove(min_val)
        return min_val
    
    def peek(self):
        return min(self.heap) if self.heap else None
    
# Better approach - Heapq

import heapq

class HeapqMinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self, val):
        heapq.heappush(self.heap, val)
        
    def extract_min(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)
    
    def peek(self):
        return self.heap[0] if self.heap else None