from sys import maxsize as maxint
from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []  # type: List[TreeNode]
        prev = -maxint
        min_diff = maxint
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            min_diff = min(min_diff, curr.val-prev)
            prev = curr.val
            if curr.right:
                root = curr.right
        return min_diff
