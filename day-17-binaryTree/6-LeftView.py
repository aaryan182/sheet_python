# Right/Left View of BT

# Assuming standing on the right side of a binary tree and given its root, return the values of the nodes visible, arranged from top to bottom.

# Examples:
# Input : root = [1, 2, 3, null, 5, null, 4]

# Output : [1, 3, 4]

def leftSideView(root):
    result = []
    
    def dfs(node, level):
        if not node:
            return

        if level == len(result):
            result.append(node.val)
        
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root,0)
    return result

# right side view 

def rightSideView(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        if level == len(result):
            result.append(node.val)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    
    dfs(root, 0)
    return result
