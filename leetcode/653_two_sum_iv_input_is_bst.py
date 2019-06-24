from typing import Generator


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        small_gen = self.small_to_big(root)
        big_gen = self.big_to_small(root)
        small = next(small_gen)
        big = next(big_gen)
        while small != big:
            curr_sum = small + big
            if curr_sum == k:
                return True
            if curr_sum > k:
                big = next(big_gen)
            else:
                small = next(small_gen)
        return False

    def small_to_big(self, node: TreeNode) -> Generator[int, None, None]:
        if node.left:
            yield from self.small_to_big(node.left)
        yield node.val
        if node.right:
            yield from self.small_to_big(node.right)

    def big_to_small(self, node: TreeNode) -> Generator[int, None, None]:
        if node.right:
            yield from self.big_to_small(node.right)
        yield node.val
        if node.left:
            yield from self.big_to_small(node.left)
