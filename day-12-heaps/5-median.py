# leetcode 295

import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2
        if n % 2 == 1:
            return float(self.nums[mid])
        else:
            return (self.nums[mid - 1] + self.nums[mid]) / 2

import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  
        self.minHeap = []  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2