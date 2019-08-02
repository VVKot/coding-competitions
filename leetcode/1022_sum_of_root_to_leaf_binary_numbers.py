class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = []

        def process_all_paths(node, path):
            if node:
                path += str(node.val)
                if not node.right and not node.left:
                    paths.append(path)
                else:
                    process_all_paths(node.left, path)
                    process_all_paths(node.right, path)
        process_all_paths(root, "")
        return sum(int(path, 2) for path in paths) if paths else 0
