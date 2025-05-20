# leetcode 493

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            count = merge_sort(low,mid) + merge_sort(mid+1, high)

            j = mid + 1
            for i in range(low, mid+1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            temp = []
            i, j = low, mid + 1
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= high:
                temp.append(nums[j])
                j += 1
            nums[low:high+1] = temp
            return count

        return merge_sort(0, len(nums) - 1)