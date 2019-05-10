class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val != val:
                return False
            stack.append(curr.right)
            stack.append(curr.left)
        return True
