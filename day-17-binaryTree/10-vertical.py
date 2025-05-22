# leetcode 987

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        column_map = defaultdict(list)
        queue =  deque([(root, 0 , 0)])

        while queue:
            node , x, y= queue.popleft()
            column_map[x].append((y, node.val))

            if node.left:
                queue.append((node.left, x - 1, y + 1))
            if node.right:
                queue.append((node.right, x + 1, y + 1))
            
        result = []

        for x in sorted(column_map.keys()):
            column = sorted(column_map[x], key= lambda k: (k[0], k[1]))
            result.append([val for y, val in column])
        
        return result
