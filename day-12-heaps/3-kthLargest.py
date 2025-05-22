# leetcode 215 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
    

#  TLE
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quickSelect(left, pivot_index - 1, k_smallest)
            else:
                return quickSelect(pivot_index + 1, right, k_smallest)
        
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            store_index = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            nums[right], nums[store_index] = nums[store_index], nums[right]  
            return store_index
        
        return quickSelect(0, len(nums) - 1, len(nums) - k)