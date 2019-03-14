class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        result = []
        if not root:
            return result
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            result.append(curr.val)
            root = curr.right
        return result
