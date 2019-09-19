class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        node_count = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                node_count += 1
                stack.append(curr.left)
                stack.append(curr.right)
        return node_count
