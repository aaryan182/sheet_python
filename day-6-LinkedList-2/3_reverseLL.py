# leetcode 25

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        while count >= k:
            curr = prev.next
            nex = curr.next
            for _ in range(k-1):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count -= k
        
        return dummy.next