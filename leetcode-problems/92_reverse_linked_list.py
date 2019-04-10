# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        for _ in range(m - 1):
            head = head.next
            prev = prev.next

        for _ in range(n - m):
            temp = head.next
            head.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
