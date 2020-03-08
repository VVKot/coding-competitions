import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        q = collections.deque([(root, 1)])
        curr_level = best_level = 1
        best_sum = curr_sum = 0
        while q:
            curr, level = q.pop()
            if level != curr_level:
                if curr_sum > best_sum:
                    best_sum = curr_sum
                    best_level = curr_level
                curr_sum = 0
                curr_level = level
            if curr:
                curr_sum += curr.val
                q.appendleft((curr.left, level+1))
                q.appendleft((curr.right, level+1))
        return best_level
