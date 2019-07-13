class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self,
                             root: TreeNode,
                             p: TreeNode,
                             q: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        ancestor_left = self.lowestCommonAncestor(root.left, p, q)
        ancestor_right = self.lowestCommonAncestor(root.right, p, q)
        if ancestor_left and ancestor_right:
            return root
        return ancestor_left or ancestor_right
