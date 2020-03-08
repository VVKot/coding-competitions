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
        smaller, greater = sorted([p.val, q.val])
        while not smaller <= root.val <= greater:
            if root.val > greater:
                root = root.left
            else:
                root = root.right
        return root
