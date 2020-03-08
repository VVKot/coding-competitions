"""
T: O(N)
S: O(N)

First, find all true values of nodes.
After that, check against the set of nodes.
"""


from typing import Set


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        self.seen_nodes = set()  # type: Set[int]
        nodes_to_visit = [(root, 0)]
        while nodes_to_visit:
            curr, val = nodes_to_visit.pop()
            if curr:
                self.seen_nodes.add(val)
                nodes_to_visit.append((curr.left, val*2+1))
                nodes_to_visit.append((curr.right, val*2+2))

    def find(self, target: int) -> bool:
        return target in self.seen_nodes
