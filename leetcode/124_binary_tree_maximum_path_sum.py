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
            left = max(0, get_val(node.left))
            right = max(0, get_val(node.right))
            self.res = max(self.res, node.val + left + right)
            return node.val + max(left, right)
        get_val(root)
        return self.res
