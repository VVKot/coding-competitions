class Node:

    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        node_map = dict()
        curr = head
        while curr:
            new = Node(curr.val, None, None)
            node_map[curr] = new
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        return node_map[head]
