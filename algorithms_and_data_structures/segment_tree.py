from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        self._build_tree(nums)

    def _build_tree(self, nums: List[int]) -> None:
        for i in reversed(range(1, self.n)):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def get_range_sum(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        range_sum = 0
        while left <= right:
            if left & 1:
                range_sum += self.tree[left]
                left += 1
            if not right & 1:
                range_sum += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return range_sum
