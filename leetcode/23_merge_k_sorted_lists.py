import heapq
from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(-1)
        if not any(lists):
            return dummy.next
        nums = []
        for i, node in enumerate(lists):
            if node:
                nums.append((node.val, i, node))
        heapq.heapify(nums)
        while nums:
            _, list_idx, node = heapq.heappop(nums)
            curr.next = node
            curr = curr.next
            next_node = node.next
            if next_node:
                heapq.heappush(nums, (next_node.val, list_idx, next_node))
        return dummy.next
