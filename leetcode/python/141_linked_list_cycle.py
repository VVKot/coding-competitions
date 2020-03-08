class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast and slow and fast == slow:
                return True
        return False
