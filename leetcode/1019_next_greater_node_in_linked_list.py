"""
T: O(N)
S: O(N)

Remember seen nodes. If we see a node that is greater than some of the seen
ones - update their next larger nodes with the value of the current node.
"""

from typing import List, Tuple


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        next_larger, stack = [], []  # type: List[int], List[Tuple[int, int]]
        while head:
            while stack and stack[-1][1] < head.val:
                next_larger[stack.pop()[0]] = head.val
            stack.append((len(next_larger), head.val))
            next_larger.append(0)
            head = head.next
        return next_larger
