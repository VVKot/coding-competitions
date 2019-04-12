class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):
        result = []
        stack = [(root, 0)]
        while stack:
            curr, level = stack.pop(0)
            if not curr:
                continue
            if len(result) <= level:
                result.append([curr.val])
            else:
                result[level].append(curr.val)
            stack.append((curr.left, level+1))
            stack.append((curr.right, level+1))
        return [sum(a)/len(a) for a in result]
