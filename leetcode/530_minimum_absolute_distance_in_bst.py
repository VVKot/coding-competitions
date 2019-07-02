class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        values = []

        def inorder(node: TreeNode) -> None:
            if node.left:
                inorder(node.left)
            values.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return min(abs(a - b) for a, b in zip(values, values[1:]))
