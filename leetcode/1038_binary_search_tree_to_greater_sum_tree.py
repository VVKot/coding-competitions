class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def helper(self, node: TreeNode, add_sum: int) -> int:
        if not node:
            return 0
        original = node.val
        right_sum = self.helper(node.right, add_sum)
        node.val += right_sum + add_sum
        left_sum = self.helper(node.left, node.val)
        return original + right_sum + left_sum

    def bstToGst(self, root: TreeNode) -> TreeNode:
        _ = self.helper(root, 0)
        return root
