class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.w_root = 0
        self.w_left = 0
        self.w_right = 0

        def with_root(node):
            if node and node.val != x:
                self.w_root += 1
                with_root(node.left)
                with_root(node.right)
        with_root(root)

        def with_left(node, add):
            if node:
                if add:
                    self.w_left += 1
                if node.val == x:
                    with_left(node.left, True)
                else:
                    with_left(node.right, add)
                    with_left(node.left, add)
        with_left(root, False)

        def with_right(node, add):
            if node:
                if add:
                    self.w_right += 1
                if node.val == x:
                    with_right(node.right, True)
                else:
                    with_right(node.right, add)
                    with_right(node.left, add)
        with_right(root, False)
        return max([self.w_root, self.w_left, self.w_right]) > n//2
