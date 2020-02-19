"""
T: O(N)
S: O(N)

Simple recursive solution based on determining the depth of subtrees.
If some subtree is inbalanced - mark its depth as such and propagate it.
"""

from typing import Dict, Optional


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        node_depth = {None: 0}  # type: Dict[Optional[TreeNode], int]
        nodes_to_process = [(root, False)]
        while nodes_to_process:
            curr, is_processed = nodes_to_process.pop()
            if not curr:
                continue
            if is_processed:
                left = node_depth[curr.left]
                right = node_depth[curr.right]
                if abs(left - right) > 1:
                    return False
                node_depth[curr] = 1 + max(left, right)
            else:
                nodes_to_process.append((curr, True))
                nodes_to_process.append((curr.left, False))
                nodes_to_process.append((curr.right, False))
        return True
