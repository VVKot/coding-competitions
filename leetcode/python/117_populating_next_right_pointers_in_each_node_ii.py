from typing import Optional


class Node:

    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: Node) -> Optional[Node]:
        curr = root  # type: Optional[Node]
        prev = None  # type: Optional[Node]
        head = None  # type: Optional[Node]
        while curr:
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                curr = curr.next
            curr = head
            head = prev = None
        return root
