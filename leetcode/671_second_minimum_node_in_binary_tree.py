class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result = -1
        if not root:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val > root.val:
                if result == -1:
                    result = curr.val
                else:
                    result = min(result, curr.val)
            else:
                stack.append(curr.left)
                stack.append(curr.right)
        return result
