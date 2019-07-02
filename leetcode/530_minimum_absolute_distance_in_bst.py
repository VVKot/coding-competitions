class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = float('inf')
        values = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            values.append(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)
        values.sort()
        for i, val in enumerate(values):
            if i != 0:
                curr_diff = abs(val - values[i-1])
                min_diff = min(min_diff, curr_diff)
        return min_diff
