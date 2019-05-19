import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []  # type: List[int]
        q = collections.deque([(root, 1)])
        while q:
            node, lvl = q.popleft()
            if node:
                if len(result) < lvl:
                    result.append(node.val)
                else:
                    result[lvl-1] = max(result[lvl-1], node.val)
                q.append((node.left, lvl+1))
                q.append((node.right, lvl+1))
        return result
