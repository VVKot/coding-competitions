"""
T: O(N)
S: O(N)

We do in-order traversal of the BST and relink nodes as we visit them.
"""


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeToDoublyList(self, root: Node) -> Node:
        if not root:
            return root
        stack = []
        head = prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            if prev:
                prev.right = curr
                curr.left = prev
            else:
                head = curr
            prev = curr
            root = curr.right
        prev.right, head.left = head, prev
        return head
