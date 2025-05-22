# Top View of BT

# Given the root of a binary tree, return the top view of the binary tree.

# Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree and are at the same position then consider the left ones only(i.e. leftmost). 

# Examples:
# Input : root = [1, 2, 3, 4, 5, 6, 7]

# Output : [4, 2, 1, 3, 7]

from collections import deque

def topView(root):
    if not root:
        return []
    
    hd_map = {}
    queue = deque([(root, 0)])
    
    while queue:
        node, hd = queue.popleft()
        
        if hd not in hd_map:
            hd_map[hd] = node.val
            
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
            
    return [hd_map[k] for k in sorted(hd_map)]