from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        right_side_view = []  # type: List[int]
        stack = [(root, 1)]
        while stack:
            curr, depth = stack.pop()
            if curr:
                if len(right_side_view) < depth:
                    right_side_view.append(curr.val)
                stack.append((curr.left, depth+1))
                stack.append((curr.right, depth+1))
        return right_side_view
