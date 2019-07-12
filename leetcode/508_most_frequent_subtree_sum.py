import collections
from typing import List, Tuple


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        _, sums = self.get_subtree_sums(root)
        result = []  # type: List[int]
        if not sums:
            return result
        sums_count = collections.Counter(sums)
        max_count = max(sums_count.values())
        for num, count in sums_count.items():
            if count == max_count:
                result.append(num)
        return result

    def get_subtree_sums(self, root: TreeNode) -> Tuple[int, List[int]]:
        if not root:
            return 0, []
        left_total, left_sums = self.get_subtree_sums(root.left)
        right_total, right_sums = self.get_subtree_sums(root.right)
        total = left_total + right_total + root.val
        return total, left_sums + right_sums + [total]
