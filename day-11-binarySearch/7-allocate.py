# Book Allocation Problem

# Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.



# Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.


# Examples:
# Input: nums = [12, 34, 67, 90], m=2

# Output: 113

# Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

# Input: nums = [25, 46, 28, 49, 24], m=4

# Output: 71

# Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.

def is_possible(nums, m , max_pages):
    count = 1
    pages_sum = 0
    
    for pages in nums:
        if pages > max_pages:
            return False
        if pages_sum + pages > max_pages:
            count += 1
            pages_sum = pages
        else:
            pages_sum += pages
        
    return count <= m

def book_allocation(nums, m):
    if m > len(nums):
        return -1
    
    low = max(nums)
    high = sum(nums)
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(nums, m , mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result