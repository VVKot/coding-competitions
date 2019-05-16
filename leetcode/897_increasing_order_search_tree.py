from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = prev = TreeNode(-1)
        stack = []  # type: List[TreeNode]
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            prev.right, prev = curr, curr
            prev.left = None
            root = curr.right
        return new_root.right
