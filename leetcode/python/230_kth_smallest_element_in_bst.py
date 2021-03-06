# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            root = curr.right
