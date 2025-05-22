# Pre, Post, Inorder in one traversal

# Given a binary tree with root node. Return the In-order,Pre-order and Post-order traversal of the binary tree.


# Examples:
# Input : root = [1, 3, 4, 5, 2, 7, 6 ]

# Output : [ [5, 3, 2, 1, 7, 4, 6] , [1, 3, 5, 2, 4, 7, 6] , [5, 2, 3, 7, 6, 4, 1] ]

# Explanation : The In-order traversal is [5, 3, 2, 1, 7, 4, 6].

# The Pre-order traversal is [1, 3, 5, 2, 4, 7, 6].

# The Post-order traversal is [5, 2, 3, 7, 6, 4, 1].

def all_traversals(root):
    if not root:
        return [], [], []
    
    preorder, inorder, postorder = [], [], []
    stack = [(root, 1)]
    
    while stack:
        node, state = stack.pop()
    
        if state == 1:
            preorder.append(node.val)
            stack.append((node, 2))
            if node.left:
                stack.append((node.left, 1))
        
        elif state == 2:
            inorder.append(node.val)
            stack.append((node, 3))
            if node.right:
                stack.append((node.right, 1))
        
        else:
            postorder.append(node.val)
    
    return [inorder, preorder, postorder]