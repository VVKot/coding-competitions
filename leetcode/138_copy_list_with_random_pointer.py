class Node:

    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        self.add_copies(head)
        self.create_random_links(head)
        new_head = head.next
        self.separate_lists(head)
        return new_head

    def add_copies(self, head: Node) -> None:
        while head:
            copied = Node(head.val, head.next, None)
            head.next, head = copied, head.next

    def create_random_links(self, head: Node) -> None:
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

    def separate_lists(self, head: Node) -> None:
        while head and head.next:
            head.next, head = head.next.next, head.next
