"""
T: O(N)
S: O(N)

Simple recursive solution based on determining the depth of subtrees.
If some subtree is inbalanced - mark its depth as such and propagate it.
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    INBALANCED_MARK = -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.get_depth(root) != self.INBALANCED_MARK

    def get_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        if left == self.INBALANCED_MARK or right == self.INBALANCED_MARK or abs(left - right) > 1:
            return self.INBALANCED_MARK
        return 1 + max(left, right)
