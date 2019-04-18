class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def pad_with_zeros(self, n, root):
        for i in range(n):
            new = ListNode(0)
            new.next = root
            root = new
        return root
    
    def get_len(self, root):
        l = 0
        while root:
            l += 1
            root = root.next
        return l
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_len = self.get_len(l1)
        l2_len = self.get_len(l2)
        l1 = self.pad_with_zeros(l2_len-l1_len, l1)
        l2 = self.pad_with_zeros(l1_len-l2_len, l2)
        carry, head = self.combine_lists(l1, l2)
        if carry > 0:
            new_head = ListNode(carry)
            new_head.next = head
            return new_head
        return head
    
    def combine_lists(self, l1, l2):
        if not l1 and not l2:
            return (0, None)
        carry, next_node = self.combine_lists(l1.next, l2.next)
        sum_ = l1.val + l2.val + carry
        new_carry, curr_value = divmod(sum_, 10)
        curr = ListNode(curr_value)
        curr.next = next_node
        return (new_carry, curr)