class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root):
        result = []
        stack = [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if not curr:
                continue
            if len(result) < level + 1:
                result.append([])
            result[level].append(curr.val)
            stack.append((curr.right, level+1))
            stack.append((curr.left, level+1))
        return result
