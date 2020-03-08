from collections import deque


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([(p, q)])
        while queue:
            lroot, rroot = queue.popleft()
            if lroot and rroot:
                if lroot.val != rroot.val:
                    return False
            elif lroot or rroot:
                return False
            else:
                continue
            queue.append((lroot.left, rroot.left))
            queue.append((lroot.right, rroot.right))
        return True
