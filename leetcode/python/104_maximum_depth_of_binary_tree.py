from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        stack = deque([(root, 1)])
        while stack:
            curr, curr_depth = stack.popleft()
            if not curr:
                continue
            if not curr.left and not curr.right:
                depth = curr_depth
            else:
                stack.append((curr.left, curr_depth + 1))
                stack.append((curr.right, curr_depth + 1))
        return depth
