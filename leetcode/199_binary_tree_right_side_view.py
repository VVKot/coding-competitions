from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []  # type: List[int]
        stack = [(root, 1)]
        while stack:
            curr, lvl = stack.pop()
            if curr:
                if lvl > len(result):
                    result.append(curr.val)
                if curr.left:
                    stack.append((curr.left, lvl + 1))
                if curr.right:
                    stack.append((curr.right, lvl + 1))
        return result
