import collections
from typing import List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        right_side_view = []  # type: List[int]
        if not root:
            return right_side_view
        queue = collections.deque([root])
        while queue:
            curr_len = len(queue)
            for i in range(curr_len):
                node = queue.popleft()
                if i == 0:
                    right_side_view.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return right_side_view
