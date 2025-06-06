# leetcode 215

import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_smallest_target_index = len(nums) - k

        def quickSelect(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            pivot_value = nums[pivot_index]
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            
            lt = left 
            i = left + 1 
            gt = right 
            
            while i <= gt:
                if nums[i] < pivot_value:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot_value:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else: 
                    i += 1
            
            if k_smallest_target_index < lt:
                return quickSelect(left, lt - 1)
            elif k_smallest_target_index > gt:
                return quickSelect(gt + 1, right)
            else:
                return pivot_value 

        return quickSelect(0, len(nums) - 1)