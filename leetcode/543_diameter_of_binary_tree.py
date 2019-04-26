class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root):
        self.res = 1

        def get_depth(node):
            if not node:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)
            self.res = max(self.res, left+right+1)
            return 1 + max(left, right)
        get_depth(root)
        return self.res - 1
