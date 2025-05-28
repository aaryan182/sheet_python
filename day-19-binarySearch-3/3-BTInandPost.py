# leetcode 106

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        inorder_map = {val: idx for idx , val in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_idx 
            if left > right:
                return None
            
            root_val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(root_val)

            index = inorder_map[root_val]

            root.right = build(index + 1, right)
            root.left = build(left, index - 1)

            return root
        
        return build(0, len(inorder) - 1)