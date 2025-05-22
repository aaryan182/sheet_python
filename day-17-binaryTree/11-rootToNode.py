# Print root to node path in BT

# Given the root of a binary tree. Return all the root-to-leaf paths in the binary tree.

# A leaf node of a binary tree is the node which does not have a left and right child.

# Examples:
# Input : root = [1, 2, 3, null, 5, null, 4]

# Output : [ [1, 2, 5] , [1, 3, 4] ]

# Explanation : There are only two paths from root to leaf.

# From root 1 to 5 , 1 -> 2 -> 5.

# From root 1 to 4 , 1 -> 3 -> 4.

def binaryTreePaths(root):
    if not root:
        return []
    
    result = []
    stack = [(root, [root.val])]
    
    while stack:
        node, path = stack.pop()

        if not node.left and not node.right:
            result.append(path)
        
        if node.right:
            stack.append((node.right, path + [node.right.val]))
        if node.left:
            stack.append((node.left, path + [node.left.val]))
    
    return result