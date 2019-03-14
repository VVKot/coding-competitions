"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:
                stack.extend(curr.children[::-1])
        return result
        