class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.left or root.right:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
        if root.left or root.right:
            return root
        return root if root.val == 1 else None
