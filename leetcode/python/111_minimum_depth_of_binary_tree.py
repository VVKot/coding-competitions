import collections


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes_queue = collections.deque([(root, 1)])
        while nodes_queue:
            curr, level = nodes_queue.pop()
            if not curr.left and not curr.right:
                return level
            if curr.left:
                nodes_queue.appendleft((curr.left, level+1))
            if curr.right:
                nodes_queue.appendleft((curr.right, level+1))
        return -1  # unreachable
