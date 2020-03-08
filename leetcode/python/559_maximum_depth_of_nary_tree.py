from collections import deque


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        depth = 0
        if not root:
            return depth
        q = deque([(root, depth + 1)])
        while q:
            curr, curr_depth = q.popleft()
            if not curr.children:
                depth = curr_depth
            else:
                for child in curr.children:
                    q.append((child, curr_depth + 1))
        return depth
