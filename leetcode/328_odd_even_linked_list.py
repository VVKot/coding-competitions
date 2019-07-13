class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        event_start = head.next
        curr = odd_end = head
        index = 1
        while curr and curr.next:
            if index & 1:
                odd_end = curr.next.next or curr
            index += 1
            next_node = curr.next
            curr.next = curr.next.next
            curr = next_node
        odd_end.next = event_start
        return head
