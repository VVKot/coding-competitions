import math
from typing import List


class IntervalTreeNode:

    def __init__(self, val: int, left: int, right: int):
        self.val = val
        self.left = left
        self.right = right


class IntervalTree:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        N = len(nums)
        leaf_count = 2 ** math.ceil(math.log(N, 2))
        self.size = 2 * leaf_count - 1
        self.nodes = [None] * self.size
        self._construct_tree(nums)

    def _construct_tree(self, nums: List[int]) -> None:

        def helper(l, r, pos):
            if l == r:
                self.nodes[pos] = IntervalTreeNode(nums[l], l, r)
                return nums[l]
            else:
                mid = (l+r) // 2
                left_val = helper(l, mid, pos*2 + 1)
                right_val = helper(mid+1, r, pos*2 + 2)
                total = left_val + right_val
                self.nodes[pos] = IntervalTreeNode(total, l, r)
                return total
        _ = helper(0, len(nums)-1, 0)

    def get_value(self, left: int, right: int) -> int:

        def helper(l, r, pos):
            node = self.nodes[pos]
            if node.right < l or node.left > r:
                return 0
            if l <= node.left and node.right <= r:
                return node.val
            left_val = helper(l, r, pos*2 + 1)
            right_val = helper(l, r, pos*2 + 2)
            return left_val + right_val

        return helper(left, right, 0)

    def update(self, i: int, diff: int) -> None:

        def helper(pos):
            node = self.nodes[pos]
            if node.left <= i <= node.right:
                node.val += diff
                if i == node.left == node.right:
                    return
                helper(pos*2 + 1)
                helper(pos*2 + 2)

        helper(0)


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = IntervalTree(nums)

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        self.tree.update(i, diff)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.get_value(i, j)
