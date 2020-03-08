class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        list_length = self.get_len(head)
        dummy = ListNode(-1)
        dummy.next = head
        step = 1
        while step < list_length:
            curr = dummy.next
            tail = dummy
            while curr:
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)
                tail = self.merge(left, right, tail)
            step <<= 1
        return dummy.next

    def get_len(self, head):
        list_length, curr = 0, head
        while curr:
            list_length += 1
            curr = curr.next
        return list_length

    def split(self, head: ListNode, n: int) -> ListNode:
        i = 1
        while head and i < n:
            head = head.next
            i += 1
        if not head:
            return head
        after = head.next
        head.next = None
        return after

    def merge(self, l1: ListNode, l2: ListNode, head: ListNode) -> ListNode:
        while l1 and l2:
            if l1.val < l2.val:
                head.next, l1 = l1, l1.next
            else:
                head.next, l2 = l2, l2.next
            head = head.next
        head.next = l1 or l2
        while head.next:
            head = head.next
        return head
