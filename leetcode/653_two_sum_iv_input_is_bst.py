from typing import Set


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()  # type: Set[int]
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val in seen:
                return True
            seen.add(k - curr.val)
            if curr.val / 2 > k:
                stack.append(curr.right)
                stack.append(curr.left)
            else:
                stack.append(curr.left)
                stack.append(curr.right)
        return False
