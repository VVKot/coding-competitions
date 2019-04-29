from typing import Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = [root]
        vals = {}  # type: Dict[TreeNode, int]
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in vals:
                stack.append(curr.left)
            elif curr.right and curr.right not in vals:
                stack.append(curr.right)
            else:
                head = stack.pop()
                left = vals[head.left] if head.left in vals else 0
                right = vals[head.right] if head.right in vals else 0
                vals[head] = 1 + max(left, right)
                res = max(res, left + right)
        return res
