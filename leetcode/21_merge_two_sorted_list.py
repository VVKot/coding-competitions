class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = head = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next, l1 = l1, l1.next
            else:
                head.next, l2 = l2, l2.next
            head = head.next
        head.next = l1 or l2
        return temp.next
