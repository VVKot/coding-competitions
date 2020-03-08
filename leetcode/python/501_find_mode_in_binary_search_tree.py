import collections
from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findMode(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        values_count = collections.Counter()

        def traverse(node):
            if node:
                values_count[node.val] += 1
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        max_count = max(values_count.values())
        for val, count in values_count.most_common():
            if count == max_count:
                result.append(val)
        return result
