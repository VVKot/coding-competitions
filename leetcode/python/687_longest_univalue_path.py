"""
T: O(N)
S: O(N)

For each node, we determine the length of "arrow", which is the length of the
maximum path starting from the current node. Notice that if values of node and
its children differ the arrow length is always 0. Also, at each node check the
maximum possible length path which is a sum of paths to the left and right.
"""

from typing import Dict, Optional


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        stack = [(root, False)]
        processed = {None: 0}  # type: Dict[Optional[TreeNode], int]
        mx = 0
        while stack:
            node, is_processed = stack.pop()
            if not node:
                continue
            left, right = node.left, node.right
            if is_processed:
                left_path_len = processed[left]
                right_path_len = processed[right]
                left_arrow = right_arrow = 0
                if left and left.val == node.val:
                    left_arrow = left_path_len + 1
                if right and right.val == node.val:
                    right_arrow = right_path_len + 1
                mx = max(mx, left_arrow + right_arrow)
                processed[node] = max(left_arrow, right_arrow)
            else:
                stack += (node, True),
                stack += (left, False),
                stack += (right, False),
        return mx
