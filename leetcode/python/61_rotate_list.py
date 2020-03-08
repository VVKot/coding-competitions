class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        ll_len = 1
        tail = head
        while tail.next:
            tail = tail.next
            ll_len += 1
        tail.next = head
        k %= ll_len
        for _ in range(ll_len-k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
