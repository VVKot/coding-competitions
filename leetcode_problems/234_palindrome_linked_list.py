class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        reverse = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        # list is of odd length
        if fast:
            slow = slow.next
        while reverse and reverse.val == slow.val:
            slow = slow.next
            reverse = reverse.next
        return not reverse