from typing import Dict, Optional


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTilt(self, root: TreeNode) -> int:
        subtree_sums = {None: 0}  # type: Dict[Optional[TreeNode], int]
        stack = [(root, False)]
        tilt = 0
        while stack:
            curr, is_processed = stack.pop()
            if curr:
                if is_processed:
                    left_sum = subtree_sums[curr.left]
                    right_sum = subtree_sums[curr.right]
                    tilt += abs(left_sum - right_sum)
                    subtree_sums[curr] = curr.val + left_sum + right_sum
                else:
                    stack.append((curr, True))
                    stack.append((curr.left, False))
                    stack.append((curr.right, False))
        return tilt
