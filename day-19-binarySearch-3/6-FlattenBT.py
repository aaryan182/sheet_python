# leetcode 114

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None

        def reversePreorder(node):
            nonlocal prev
            if not node:
                return
            
            reversePreorder(node.right)
            reversePreorder(node.left)

            node.right = prev
            node.left = None
            prev = node

        reversePreorder(root)
        