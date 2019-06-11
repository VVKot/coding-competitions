class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        before_mid = self.get_before_mid(head)
        mid = before_mid.next
        before_mid.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge_lists(left, right)

    def get_before_mid(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge_lists(self, left: ListNode, right: ListNode) -> ListNode:
        curr = dummy = ListNode(-1)
        while left and right:
            if left.val < right.val:
                curr.next, left = left, left.next
            else:
                curr.next, right = right, right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next
