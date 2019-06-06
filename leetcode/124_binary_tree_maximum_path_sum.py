class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')

        def get_val(node):
            if not node:
                return 0
            left = get_val(node.left)
            right = get_val(node.right)
            val = node.val
            val_left, val_right = val + left, val + right
            val_left_right = val + left + right
            propagate = max([val, val_left, val_right])
            self.res = max([self.res, propagate, val_left_right])
            return propagate
        get_val(root)
        return self.res
