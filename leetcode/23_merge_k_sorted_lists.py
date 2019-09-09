from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not any(lists):
            return None
        K = len(lists)
        step = 1
        while step < K:
            for i in range(0, K-step, step*2):
                lists[i] = self.merge(lists[i], lists[i+step])
            step *= 2
        return lists[0]

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummy = new_head = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                new_head.next, head1 = head1, head1.next
            else:
                new_head.next, head2 = head2, head2.next
            new_head = new_head.next
        new_head.next = head1 or head2
        return dummy.next
