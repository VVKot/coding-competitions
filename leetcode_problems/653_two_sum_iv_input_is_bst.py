class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        stack = [root]
        seen = set()
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val in seen:
                return True
            seen.add(k-curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
        return False
