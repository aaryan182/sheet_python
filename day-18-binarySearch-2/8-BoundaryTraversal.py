# Boundary Traversal

# Given a root of Binary Tree, perform the boundary traversal of the tree. 



# The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.



# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

# The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
# If a node in the left boundary and has a left child, then the left child is in the left boundary.
# If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
# The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.


# Examples:
# Input : root = [1, 2, 3, 4, 5, 6, 7, null, null, 8, 9]

# Output : [1, 2, 4, 8, 9, 6, 7, 3]

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isLeaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None

def addLeftBoundary(node: TreeNode, boundary: List[int]):
    while node:
        if not isLeaf(node):
            boundary.append(node.val)
        node = node.left if node.left else node.right

def addLeaves(node: TreeNode, boundary: List[int]):
    if node is None:
        return
    if isLeaf(node):
        boundary.append(node.val)
    else:
        addLeaves(node.left, boundary)
        addLeaves(node.right, boundary)

def addRightBoundary(node: TreeNode, boundary: List[int]):
    temp = []
    while node:
        if not isLeaf(node):
            temp.append(node.val)
        node = node.right if node.right else node.left
    boundary.extend(temp[::-1]) 

def boundaryTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    boundary = []
    
    if not isLeaf(root):
        boundary.append(root.val)

    addLeftBoundary(root.left, boundary)
    addLeaves(root, boundary)
    addRightBoundary(root.right, boundary)

    return boundary
