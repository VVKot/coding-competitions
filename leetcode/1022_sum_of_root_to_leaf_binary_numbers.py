class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0
        self.process_all_paths(root, 0)
        return self.result

    def process_all_paths(self, node: TreeNode, total: int) -> None:
        if node:
            total *= 2
            total += node.val
            if not node.right and not node.left:
                self.result += total
            else:
                self.process_all_paths(node.left, total)
                self.process_all_paths(node.right, total)
