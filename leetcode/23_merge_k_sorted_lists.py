from typing import List, Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not any(lists):
            return None

        N = len(lists)
        interval = 1
        while interval < N:
            for i in range(0, N - interval, interval * 2):
                lists[i] = self.merge_lists(lists[i],
                                            lists[i + interval])
            interval *= 2
        return lists[0]

    def merge_lists(self, head1, head2):
        curr = dummy = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1:
            curr.next = head1
        if head2:
            curr.next = head2
        return dummy.next
