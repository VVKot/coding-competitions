class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            first, second = stack.pop()
            if not first and not second:
                continue

            if not first or not second:
                return False

            if first.val != second.val:
                return False

            stack.append((first.left, second.right))
            stack.append((first.right, second.left))
        return True
