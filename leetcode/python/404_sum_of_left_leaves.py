"""
T: O(N)
S: O(N)

Walk through the whole tree and check every node marking their relation to the
parent. If a given node is not a leaf, add its children to processing. If it is
a leaf - check if it is a left leaf, and if so - add its value to the sum.
"""


class TreeNode:

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, False)]
        while stack:
            curr, is_left = stack.pop()
            if not curr:
                continue
            if curr.left or curr.right:
                stack.append((curr.left, True))
                stack.append((curr.right, False))
            elif is_left:
                result += curr.val
        return result
