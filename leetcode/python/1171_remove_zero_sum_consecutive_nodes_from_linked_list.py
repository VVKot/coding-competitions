from typing import Dict


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        seen = {}  # type: Dict[int, ListNode]
        while curr:
            prefix_sum += curr.val
            node = seen.get(prefix_sum, curr)
            while prefix_sum in seen:
                seen.popitem()
            seen[prefix_sum] = node
            node.next, curr = curr.next, curr.next
        return dummy.next
