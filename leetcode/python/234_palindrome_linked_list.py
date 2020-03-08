class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        list_representation = []
        while head:
            list_representation.append(head.val)
            head = head.next
        left, right = 0, len(list_representation)-1
        while left < right:
            if list_representation[left] != list_representation[right]:
                return False
            left += 1
            right -= 1
        return True
