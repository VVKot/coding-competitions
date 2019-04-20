class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        before = head
        last = head
        while n:
            n -= 1
            last = last.next
        if not last:
            return head.next
        while last.next:
            before = before.next
            last = last.next
        before.next = before.next.next
        return head
