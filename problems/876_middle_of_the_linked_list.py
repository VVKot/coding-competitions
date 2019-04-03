class Solution:
    def middleNode(self, head):
        list_len = 0
        old_head = head
        while head:
            list_len += 1
            head = head.next
            middle_index = list_len // 2
        while middle_index != 0:
            middle_index -= 1
            old_head = old_head.next
        return old_head
