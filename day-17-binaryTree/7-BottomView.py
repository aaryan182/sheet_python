# Bottom view of BT

# Given root of binary tree, return the bottom view of the binary tree.

# The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom. Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree and are at the same position then consider the node that appears later in level traversal.

# Examples:
# Input : root = [20, 8, 22, 5, 3, null, 25, null, null, 10 ,14]

# Output : [5, 10, 3, 14, 25]

# Explanation : From left to right the path is as follows :
# First we encounter node with value 5.

# Then we have nodes 8 , 10 but from bottom only 10 will be visible.

# Next we have 20 , 3 but from bottom only 3 will be visible.

# Next we have 14 , 22 but from bottom only 14 will be visible.

# Then we encounter node with value 25.

from collections import deque

def bottomView(root):
    if not root:
        return []
    
    hd_map = {}
    
    queue = deque([root, 0])
    
    while queue:
        node, hd = queue.popLeft()
        hd_map[hd] = node.val
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
        
    return [hd_map[key] for key in sorted(hd_map)]