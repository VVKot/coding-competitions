from itertools import zip_longest
from typing import Iterable


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return all(a == b for a, b in zip_longest(
            self.preorder(root1), self.preorder(root2)))

    def preorder(self, root: TreeNode) -> Iterable[int]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                yield curr.val
            else:
                stack.append(curr.right)
                stack.append(curr.left)
