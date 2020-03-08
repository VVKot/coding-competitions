class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.is_strict_subtree(s, t) or self.isSubtree(s.left, t) \
            or self.isSubtree(s.right, t)

    def is_strict_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return not s and not t
        return s.val == t.val and self.is_strict_subtree(s.left, t.left) \
            and self.is_strict_subtree(s.right, t.right)
