# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # prev a b b.next
        prev, prev.next = self, head
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            prev.next, first.next, second.next = second, second.next, first
            prev = first
        return self.next
