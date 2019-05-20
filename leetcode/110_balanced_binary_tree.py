class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        return self.get_depth(root) != -1

    def get_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
