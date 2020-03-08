class Node:

    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: Node) -> Node:
        if not root:
            return root
        prev, curr = root, None
        while prev.left:
            curr = prev
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            prev = prev.left
        return root
