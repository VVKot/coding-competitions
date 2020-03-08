class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head):
        if not head:
            return head
        meet = self.find_meeting_point(head)
        if not meet:
            return meet
        while head != meet:
            head, meet = head.next, meet.next
        return head

    def find_meeting_point(self, head):
        slow, fast, meet = head, head, None
        while slow.next and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                meet = slow
                break
        return meet
