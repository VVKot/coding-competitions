from typing import List


class Node:

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        result = []  # type: List[int]
        if not root:
            return result
        stack = [root]
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:
                stack.extend(curr.children[::-1])
        return result
