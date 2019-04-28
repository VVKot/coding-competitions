from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rob(self, root: TreeNode) -> int:
        first, second = self.helper(root)
        return max(first, second)

    def helper(self, node: TreeNode) -> List[int]:
        if not node:
            return [0] * 2
        left_inc, left_exc = self.helper(node.left)
        right_inc, right_exc = self.helper(node.right)
        inc = node.val + left_exc + right_exc
        exc = max(left_inc, left_exc) + max(right_inc, right_exc)
        return [inc, exc]
