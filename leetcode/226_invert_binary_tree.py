"""
T: O(N)
S: O(N)

Just do as the description says.
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        nodes_to_process = [root]
        while nodes_to_process:
            curr = nodes_to_process.pop()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                nodes_to_process.append(curr.left)
                nodes_to_process.append(curr.right)
        return root
