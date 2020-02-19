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

    INBALANCED_TREE_DEPTH = -1

    def isBalanced(self, root: TreeNode) -> bool:
        nodes_values = {None: 0}  # type: Dict[Optional[TreeNode], int]
        nodes_to_process = [(root, False)]
        while nodes_to_process:
            curr, is_processed = nodes_to_process.pop()
            if not curr:
                continue
            if is_processed:
                left = nodes_values[curr.left]
                right = nodes_values[curr.right]
                if self.INBALANCED_TREE_DEPTH in [left, right] or \
                        abs(left - right) > 1:
                    nodes_values[curr] = self.INBALANCED_TREE_DEPTH
                else:
                    nodes_values[curr] = 1 + max(left, right)
            else:
                nodes_to_process.extend([(curr, True), (curr.left, False),
                                         (curr.right, False)])
        return nodes_values[root] != self.INBALANCED_TREE_DEPTH
