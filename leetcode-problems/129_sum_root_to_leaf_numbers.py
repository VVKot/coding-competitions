class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_sum(self, root, num_so_far):
        if not root.left and not root.right:
            return num_so_far
        result = 0
        if root.left:
            result += self.get_sum(root.left, num_so_far * 10 + root.left.val)
        if root.right:
            result += self.get_sum(root.right,
                                   num_so_far * 10 + root.right.val)
        return result

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = self.get_sum(root, root.val)
        return result
