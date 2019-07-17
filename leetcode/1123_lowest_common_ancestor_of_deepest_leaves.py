from typing import Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        _, lca = self.get_lca(root, 0)
        return lca

    def get_lca(self, node: TreeNode, depth: int) -> Tuple[int, TreeNode]:
        if not node:
            return depth, node
        left_depth, left_lca = self.get_lca(node.left, depth+1)
        right_depth, right_lca = self.get_lca(node.right, depth+1)
        if left_depth == right_depth:
            return left_depth, node
        if left_depth > right_depth:
            return left_depth, left_lca
        return right_depth, right_lca
