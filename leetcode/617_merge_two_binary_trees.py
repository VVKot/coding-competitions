class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        stack = [(t1, t2)]
        while stack:
            curr1, curr2 = stack.pop()
            if curr2:
                curr1.val += curr2.val
                if curr1.left:
                    stack.append((curr1.left, curr2.left))
                else:
                    curr1.left = curr2.left
                if curr1.right:
                    stack.append((curr1.right, curr2.right))
                else:
                    curr1.right = curr2.right
        return t1
