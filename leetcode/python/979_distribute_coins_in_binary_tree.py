"""
T: O(N)
S: O(N)

We need to find how far we move coins from each subtree. We find the number of
coins that we more from left and right, and add their magnitude to the result.
That's because these coins will be moved at least this number of times. After
that, we return the correct balance for the current node, which possibly will
be processed by its parent. Note that since the number of coins is guaranteed
to be the same as the number of nodes, the balance of root is guaranteed
to be zero.
"""

from typing import Dict, Optional


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def distributeCoins(self, root: TreeNode) -> int:
        distribution_cost = 0
        nodes_to_process = [root]
        nodes_balances = {None: 0}  # type: Dict[Optional[TreeNode], int]
        while nodes_to_process:
            curr = nodes_to_process[-1]
            if curr:
                left, right = curr.left, curr.right
                if left and left not in nodes_balances:
                    nodes_to_process.append(left)
                elif right and right not in nodes_balances:
                    nodes_to_process.append(right)
                else:
                    nodes_to_process.pop()
                    left_balance = nodes_balances[left]
                    right_balance = nodes_balances[right]
                    distribution_cost += abs(left_balance) + abs(right_balance)
                    nodes_balances[curr] = left_balance + right_balance + \
                        curr.val - 1
        return distribution_cost
