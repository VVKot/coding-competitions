from typing import Tuple


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTilt(self, root: TreeNode) -> int:
        _, tilt = self.get_tilt_rec(root)
        return tilt

    def get_tilt_rec(self, root: TreeNode) -> Tuple[int, int]:
        if not root:
            return 0, 0
        l_total, l_tilt = self.get_tilt_rec(root.left)
        r_total, r_tilt = self.get_tilt_rec(root.right)
        total = l_total + r_total + root.val
        tilt = abs(l_total - r_total) + l_tilt + r_tilt
        return total, tilt
