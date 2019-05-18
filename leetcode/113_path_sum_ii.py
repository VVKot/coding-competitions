from typing import List


class TreeNode:

    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        result = []  # type: List[List[int]]
        if not root:
            return result
        stack = [(root, root.val, [root.val])]
        while stack:
            node, total, path = stack.pop()
            if not node.left and not node.right:
                if total == sum_:
                    result.append(path)
            else:
                if node.left:
                    val = node.left.val
                    stack.append((node.left, total+val, path + [val]))
                if node.right:
                    val = node.right.val
                    stack.append((node.right, total+val, path + [val]))
        return result
