class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        dummy.next = head
        while head and head.next:
            prev.next = head.next
            head.next.next, head.next = head, head.next.next
            prev, head = head, head.next
        return dummy.next
