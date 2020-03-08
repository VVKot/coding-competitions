"""
T: O(N)
S: O(N)

Traverse all nodes, remember the number we have seen in the parent, calculate
the current number based on it.
"""


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        total_sum = 0
        nodes_to_process = [(root, 0)]
        while nodes_to_process:
            curr, num = nodes_to_process.pop()
            if not curr:
                continue
            curr_num = num * 10 + curr.val
            if curr.left or curr.right:
                nodes_to_process.append((curr.left, curr_num))
                nodes_to_process.append((curr.right, curr_num))
            else:
                total_sum += curr_num
        return total_sum
