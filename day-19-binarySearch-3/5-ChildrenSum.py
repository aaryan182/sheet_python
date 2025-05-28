# Check for Children Sum Property in a Binary Tree

# Problem Statement: Given a Binary Tree, convert the value of its nodes to follow the Children Sum Property. The Children Sum Property in a binary tree states that for every node, the sum of its children's values (if they exist) should be equal to the node's value. If a child is missing, it is considered as having a value of 0.

# Note:

# The node values can be increased by any positive integer any number of times, but decrementing any node value is not allowed.
# A value for a NULL node can be assumed as 0.
# We cannot change the structure of the given binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertToChildrenSumTree(root: TreeNode) -> None:
    if not root or (not root.left and not root.right):
        return

    # Step 1: Fix children first (post-order)
    convertToChildrenSumTree(root.left)
    convertToChildrenSumTree(root.right)

    # Get child values (0 if child is None)
    left_val = root.left.val if root.left else 0
    right_val = root.right.val if root.right else 0

    child_sum = left_val + right_val

    if child_sum > root.val:
        root.val = child_sum
    else:
        incrementChildren(root, root.val - child_sum)

def incrementChildren(node: TreeNode, diff: int) -> None:
    if not node:
        return

    if node.left:
        node.left.val += diff
        incrementChildren(node.left, diff)
    elif node.right:
        node.right.val += diff
        incrementChildren(node.right, diff)