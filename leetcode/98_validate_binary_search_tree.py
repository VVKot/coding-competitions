from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []  # type: List[TreeNode]
        prev = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                if prev and prev.val >= curr.val:
                    return False
                prev = curr
                root = curr.right
        return True
