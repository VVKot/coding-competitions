from sys import maxsize as maxint
from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest = []
        nodes_to_delete = set(to_delete)

        def delete_nodes(node):
            if node:
                node.left = delete_nodes(node.left)
                node.right = delete_nodes(node.right)
                if node.val in nodes_to_delete:
                    if node.left:
                        forest.append(node.left)
                    if node.right:
                        forest.append(node.right)
                    return None
                else:
                    return node

        dummy = TreeNode(maxint)
        dummy.left = root
        nodes_to_delete.add(dummy.val)
        delete_nodes(dummy)
        return forest
