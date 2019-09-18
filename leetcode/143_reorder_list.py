class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        after_mid = slow.next
        slow.next = None
        prev = None
        while after_mid:
            after_mid.next, after_mid, prev = prev, after_mid.next, after_mid
        while head and prev:
            head.next, head = prev, head.next
            prev.next, prev = head, prev.next
