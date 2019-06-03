from collections import defaultdict
from typing import List, DefaultDict, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []  # type: List[List[int]]
        if not root:
            return result
        traversal = \
            defaultdict(list)  # type: DefaultDict[List[Tuple[int, int]]]
        stack = [(root, 0, 0)]
        while stack:
            node, x, y = stack.pop()
            traversal[x].append((y, node.val))
            if node.left:
                stack.append((node.left, x - 1, y - 1))
            if node.right:
                stack.append((node.right, x + 1, y - 1))
        for k in sorted(traversal.keys()):
            result.append([val for _, val in sorted(
                traversal[k], key=self.sort_lambda)])
        return result

    def sort_lambda(self, x):
        return -x[0], x[1]
