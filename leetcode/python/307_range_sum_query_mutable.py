from typing import List


class IntervalTree:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n << 1)
        self._build_tree(nums)

    def _build_tree(self, nums: List[int]) -> None:
        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
        for i in reversed(range(1, self.n)):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 0:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def get_value(self, left: int, right: int) -> int:
        result = 0
        left += self.n
        right += self.n
        while left <= right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if not right & 1:
                result += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return result


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = IntervalTree(nums)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.get_value(i, j)
