# leetcode 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            root.left = array_to_tree(left, inorder_map[root_val] - 1)
            root.right = array_to_tree(inorder_map[root_val] + 1 , right)

            return root
        
        return array_to_tree(0, len(inorder) - 1)