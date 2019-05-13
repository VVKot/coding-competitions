from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum_ = 0
        stack = []  # type: List[TreeNode]
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            if L <= curr.val <= R:
                sum_ += curr.val
            elif curr.val > R:
                return sum_
            root = curr.right
        return sum_
