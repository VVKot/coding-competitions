from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        stack = []  # type: List[TreeNode]
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev == p.val:
                return root
            prev = root.val
            root = root.right
        return None
