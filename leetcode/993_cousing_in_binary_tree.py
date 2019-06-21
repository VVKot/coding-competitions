from typing import List, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        found = None
        stack = [(root, None, 0)]  # type: List[Tuple[TreeNode, TreeNode, int]]
        while stack:
            curr, par, lvl = stack.pop()
            if not curr:
                continue
            if curr.val == x or curr.val == y:
                if found:
                    par2, lvl2 = found
                    return lvl2 == lvl and par2 != par
                else:
                    found = (par, lvl)
            if curr.left:
                stack.append((curr.left, curr, lvl + 1))
            if curr.right:
                stack.append((curr.right, curr, lvl + 1))
        return False
