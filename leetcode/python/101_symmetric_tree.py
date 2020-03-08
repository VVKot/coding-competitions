"""
T: O(N)
S: O(N)

Start with left and right children of the root. For a tree to be symmetric
both of them should either have same value or both be emptry. If that condition
holds, check their children in mirrored fashion - first left with second right
and first right with second left.
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
