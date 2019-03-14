"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        # recursive
        # result = []
        # if not root:
        #     return result
        # for child in root.children:
        #     result += self.postorder(child)
        # result.append(root.val)
        # return result

        # iterative
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            stack.extend(curr.children)

        return result[::-1]