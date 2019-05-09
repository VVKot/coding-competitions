from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = self.get_leaves(root1)
        leaves2 = self.get_leaves(root2)
        return leaves1 == leaves2

    def get_leaves(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                result.append(curr.val)
            else:
                stack.append(curr.right)
                stack.append(curr.left)
        return result
