class Node:

    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:

    def inorderSuccessor(self, node: Node) -> Node:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        curr_val = node.val
        while node.parent and node.parent.val < curr_val:
            node = node.parent
        return node.parent
