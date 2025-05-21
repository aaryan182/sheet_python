# leetcode 138

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        while curr:
            next_node = curr.next
            copy_node = Node(curr.val)
            curr.next = copy_node
            copy_node.next = next_node
            curr = next_node

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        dummy = Node(0)
        copy_curr = dummy
        curr = head
        while curr:
            copy_node = curr.next
            copy_curr.next = copy_node
            copy_curr = copy_node

            curr.next = copy_node.next
            curr = curr.next

        return dummy.next