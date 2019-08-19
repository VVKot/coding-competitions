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

        def delete_nodes(node, is_root):
            if node:
                is_deleted = node.val in nodes_to_delete
                if not is_deleted and is_root:
                    forest.append(node)
                node.left = delete_nodes(node.left, is_deleted)
                node.right = delete_nodes(node.right, is_deleted)
                return None if is_deleted else node

        delete_nodes(root, True)
        return forest
