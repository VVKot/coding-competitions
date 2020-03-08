class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        even_head = head.next
        odd, even = head, head.next
        while even and even.next:
            odd.next, odd = even.next, even.next
            even.next, even = odd.next, odd.next
        odd.next = even_head
        return head
