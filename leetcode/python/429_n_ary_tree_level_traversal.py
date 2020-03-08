from typing import List


class Node:

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:

    def levelOrder(self, root: Node) -> List[List[int]]:
        queue, result = [root], []  # type: List[Node], List[List[int]]
        if not root:
            return result
        while queue:
            result.append([node.val for node in queue])
            queue = [child for node in queue
                     for child in node.children if child]
        return result
