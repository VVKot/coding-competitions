"""
T: O(N)
S: O(N)

The gist of the solution is to determine a correct index for each node.
Since we are doing BFS, also known as level traversal, we can simply put
the node to the appropriate bucket with the nodes of the same vertical index.
In the end, we use recorded minimum and maximum indices to get a proper order.
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
        curr_index = min_index = max_index = 0
        nodes_queue = collections.deque([(root, curr_index)])
        while nodes_queue:
            curr, index = nodes_queue.popleft()
            if not curr:
                continue
            min_index = min(min_index, index)
            max_index = max(max_index, index)
            column_order[index].append(curr.val)
            nodes_queue.append((curr.left, index - 1))
            nodes_queue.append((curr.right, index + 1))
        return [
            column_order[index] for index in range(min_index, max_index + 1)
        ]
