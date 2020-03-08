import collections
from typing import Counter, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sums_count = collections.Counter()  # type: Counter[int]

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            sums_count[total] += 1
            return total

        dfs(root)
        max_count = max(sums_count.values())
        return [_sum for _sum in sums_count if sums_count[_sum] == max_count]
