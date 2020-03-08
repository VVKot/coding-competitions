"""
T: O(N)
S: O(N)

An optimal solution that takes logarithmic time in the best case. Walk in the
appropriate direction in the BST according to the target. On each step, check
the difference and update the result if the difference is smaller than a
previously seen one. If we can assume that tree nodes only hold distinct int
values, this algorithm can be optimized with early termination. We can return
the result if we see a number within distance <= 0.5.
"""


class TreeNode:

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def closestValue(self, root: TreeNode, target: float) -> int:
        min_diff = float('inf')
        closest_value = 0
        while root:
            if not root:
                continue
            curr_diff = abs(root.val - target)
            if curr_diff < min_diff:
                min_diff = curr_diff
                closest_value = root.val
            root = root.left if root.val > target else root.right
        return closest_value
