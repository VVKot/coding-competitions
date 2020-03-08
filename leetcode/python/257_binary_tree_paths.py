from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        stack = []
        if root:
            stack.append([root])
        while stack:
            path = stack.pop()
            curr = path[-1]
            if not curr.left and not curr.right:
                result.append(self.get_formated_path(path))
            else:
                if curr.left:
                    stack.append(path + [curr.left])
                if curr.right:
                    stack.append(path + [curr.right])
        return result

    def get_formated_path(self, path):
        return '->'.join(str(node.val) for node in path)
