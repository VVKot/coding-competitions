from typing import Optional


#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        prev = None
        while head:
            prev, head.next, head = head, prev, head.next
        return prev
