"""
T: O(N)
S: O(N)

The recursive version of the solution. Find the left and right branches and
append them to the result if they are not empty. Important trick - if the left
branch is empty and right is not we have to append empty left branch to
differentiate between cases of empty left and right branch.
"""

from typing import Dict, List, Optional


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    BEGIN_BRANCH, END_BRANCH = '(', ')'

    def tree2str(self, t: TreeNode) -> str:
        nodes_to_process = [t]
        processed_nodes = {
            None: []
        }  # type: Dict[Optional[TreeNode], List[str]]
        while nodes_to_process:
            node = nodes_to_process.pop()
            if not node:
                continue
            if node.left in processed_nodes and node.right in processed_nodes:
                left, right = map(processed_nodes.get, [node.left, node.right])
                curr_subtree = [str(node.val)]
                if left or right:
                    self.add_branch(curr_subtree, left)
                if right:
                    self.add_branch(curr_subtree, right)
                processed_nodes[node] = curr_subtree
            else:
                nodes_to_process.append(node)
                nodes_to_process.append(node.right)
                nodes_to_process.append(node.left)
        return ''.join(processed_nodes[t])

    def add_branch(self, flat_tree: List[str],
                   flat_branch: List[str]) -> List[str]:
        flat_tree.append(self.BEGIN_BRANCH)
        flat_tree.extend(flat_branch)
        flat_tree.append(self.END_BRANCH)
