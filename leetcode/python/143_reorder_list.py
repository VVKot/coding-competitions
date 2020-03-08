from typing import Optional


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        mid = self.get_mid(head)
        after_mid = mid.next
        mid.next = None
        tail = self.reverse_list(after_mid)
        while head and tail:
            head.next, head = tail, head.next
            tail.next, tail = head, tail.next

    def get_mid(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, head, prev = prev, head.next, head
        return prev
