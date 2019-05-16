class Node:

    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        curr = head
        # duplicate
        while curr:
            new = Node(curr.val, curr.next, None)
            curr.next, curr = new, curr.next
        curr = head
        # copy random
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr, new_head, prev = head, head.next, None
        # restore
        while curr and curr.next:
            if prev:
                prev.next = curr.next
            prev = curr.next
            curr.next, curr = curr.next.next, curr.next.next
        return new_head
