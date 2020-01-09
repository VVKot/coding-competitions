"""
T: O(N)
S: O(N)

The recursive version of the solution. Find the left and right branches and
append them to the result if they are not empty. Important trick - if the left
branch is empty and right is not we have to append empty left branch to
differentiate between cases of empty left and right branch.
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    OPEN, CLOSE = '(', ')'

    def tree2str(self, t: TreeNode) -> str:

        def tree2str_rec(node):
            if not node:
                return []
            flattened_tree = [str(node.val)]
            left, right = map(tree2str_rec, [node.left, node.right])
            if left or right:
                flattened_tree.append(self.OPEN)
                flattened_tree.extend(left)
                flattened_tree.append(self.CLOSE)
            if right:
                flattened_tree.append(self.OPEN)
                flattened_tree.extend(right)
                flattened_tree.append(self.CLOSE)
            return flattened_tree

        flattened = tree2str_rec(t)
        return ''.join(flattened)
