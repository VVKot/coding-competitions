"""
T: O(N)
S: O(N)

Start with left and right children of the root. After that, check their
children in mirrored fashion - left with right and right with left.
"""


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
            if first and second:
                if first.val != second.val:
                    return False
                stack.append((first.left, second.right))
                stack.append((first.right, second.left))
            elif first or second:
                return False
        return True
