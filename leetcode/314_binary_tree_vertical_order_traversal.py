"""
T: O(NlogN)
S: O(N)

The gist of the solution is to determine a correct index for each node.
Since we are doing BFS, also known as level traversal, we can simply put
the node to the appropriate bucket with the nodes of the same vertical index.
In the end, we have to sort the dictionary to achieve a correct result.
"""

import collections
from typing import Dict, List


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        column_order = collections.defaultdict(
            list)  # type: Dict[int, List[int]]
        nodes_queue = collections.deque([(root, 0)])
        while nodes_queue:
            curr, index = nodes_queue.popleft()
            if not curr:
                continue
            column_order[index].append(curr.val)
            nodes_queue.append((curr.left, index - 1))
            nodes_queue.append((curr.right, index + 1))
        return [column_order[index] for index in sorted(column_order.keys())]
