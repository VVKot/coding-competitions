class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0
        self.process_all_paths(root, "")
        return self.result

    def process_all_paths(self, node: TreeNode, path: str) -> None:
        if node:
            path += str(node.val)
            if not node.right and not node.left:
                self.result += int(path, 2)
            else:
                self.process_all_paths(node.left, path)
                self.process_all_paths(node.right, path)
