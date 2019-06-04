import collections
from typing import List


class Node:

    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: Node) -> Node:
        if not root:
            return root
        queue = collections.deque([(root, 0)])
        row, curr_level = [], -1  # type: List[Node], int
        while queue:
            node, level = queue.popleft()
            if curr_level != level:
                self.process_row(row)
                row = []
                curr_level = level
            row.append(node)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        self.process_row(row)
        return root

    def process_row(self, nodes: List[Node]):
        count = len(nodes)
        for i in range(count - 1):
            nodes[i].next = nodes[i + 1]
