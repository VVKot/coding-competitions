"""
T: O(N)
S: O(N)

A good example of making a recursive solution into an iterative one.
For each node, we need to get to know the depths of their left and right
branches. Using this information, we find the diameter for the current node
and current node depth. The maximum seen diameter is the maximum diameter
of the tree.
"""


from typing import Dict, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = 0
        if not root:
            return max_diameter
        node_depths = {None: 0}  # type: Dict[Optional[TreeNode], int]
        nodes_to_process = [root]
        while nodes_to_process:
            curr = nodes_to_process[-1]
            left, right = curr.left, curr.right
            if left and left not in node_depths:
                nodes_to_process.append(left)
            elif right and right not in node_depths:
                nodes_to_process.append(right)
            else:
                _ = nodes_to_process.pop()
                left_depth = node_depths[left]
                right_depth = node_depths[right]
                node_depths[curr] = 1 + max(left_depth, right_depth)
                max_diameter = max(max_diameter, left_depth + right_depth)
        return max_diameter
